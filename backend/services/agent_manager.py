"""
Módulo principal del agente inteligente.
Genera la búsqueda de dietas usando algoritmos genéticos y recocido simulado.
"""

from models.user_input import UserInput
from services.diet_calculation import calculate_user_requirements
from services.data_loader import get_foods
from algorithms.population import generate_initial_population
from algorithms.genetic import genetic_algorithm
from algorithms.annealing import simulated_annealing
import math


# ==========================================================
# SANITIZADOR JSON – evita NaN / Inf que rompen FastAPI
# ==========================================================
def clean_for_json(obj):
    if isinstance(obj, dict):
        return {k: clean_for_json(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [clean_for_json(v) for v in obj]
    elif isinstance(obj, float):
        if math.isnan(obj) or math.isinf(obj):
            return None
    return obj


# ==========================================================
# AGENTE PRINCIPAL
# ==========================================================
def nutrition_agent(user_data: UserInput):
    print("🔍 Iniciando agente de búsqueda nutricional...")

    # --------------------------------------------------------------
    # 1. REQUERIMIENTOS
    # --------------------------------------------------------------
    print("📌 Calculando requerimientos del usuario...")
    requirements = calculate_user_requirements(user_data)

    # --------------------------------------------------------------
    # 2. ALIMENTOS
    # --------------------------------------------------------------
    print("📌 Cargando alimentos desde dataset limpio...")
    foods = get_foods()

    if not foods:
        return clean_for_json({
            "status": "error",
            "message": "No se pudieron cargar alimentos desde la base."
        })

    foods_dict = {item["id"]: item for item in foods}
    print(f"📌 {len(foods)} alimentos cargados correctamente.")

    # --------------------------------------------------------------
    # 3. POBLACIÓN INICIAL
    # --------------------------------------------------------------
    print("🧬 Generando población inicial...")
    population = generate_initial_population(
        foods=foods,
        user=user_data,
        requirements=requirements,
        size=200
    )
    print(f"🧬 Población inicial generada con {len(population)} individuos.")

    # --------------------------------------------------------------
    # 4. ALGORITMO GENÉTICO
    # --------------------------------------------------------------
    print("🧪 Ejecutando algoritmo genético...")
    top_genetic = genetic_algorithm(
        population=population,
        foods_dict=foods_dict,
        user=user_data,
        requirements=requirements,
        generations=60,
        mutation_rate=0.05,
        top_k=5
    )

    print("🧬 Dietas seleccionadas para recocido simulado:")
    for i, ind in enumerate(top_genetic, 1):
        print(f"   GA Top {i}: {ind}")

    # --------------------------------------------------------------
    # 5. RECOCIDO SIMULADO
    # --------------------------------------------------------------
    print("🔥 Ejecutando recocido simulado...")

    best_score_overall = -1
    best_diet_overall = None

    for i, diet_ids in enumerate(top_genetic, 1):
        print(f"Refinando dieta GA Top {i} con SA...")

        optimized_ids, score = simulated_annealing(
            diet_ids,
            foods_dict,
            requirements,
            user_data
        )

        if score > best_score_overall:
            best_score_overall = score
            best_diet_overall = optimized_ids

    # --------------------------------------------------------------
    # 6. CONVERTIR IDs A OBJETOS COMPLETOS
    # --------------------------------------------------------------
    final_foods = []
    if best_diet_overall:
        for fid in best_diet_overall:
            food = foods_dict.get(fid)
            if food:
                final_foods.append(food)

    print(f"🏆 Mejor dieta final con fitness {best_score_overall:.4f}")
    print("📦 Construyendo respuesta final...")

    # --------------------------------------------------------------
    # 7. RESPUESTA FINAL + SANITIZADOR JSON
    # --------------------------------------------------------------
    response = {
        "status": "ok",
        "message": "Agente ejecutado correctamente.",
        "requirements": requirements,
        "final_diet": final_foods,
        "final_fitness": best_score_overall
    }

    return clean_for_json(response)
