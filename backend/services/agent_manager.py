"""
Módulo principal del agente inteligente.
Genera la búsqueda de dietas usando algoritmos genéticos y recocido simulado.
"""

from models.user_input import UserInput
from services.diet_calculation import calculate_user_requirements
from services.data_loader import get_foods
from algorithms.population import generate_initial_population
from algorithms.genetic import genetic_algorithm
# from algorithms.annealing import simulated_annealing  # se activará luego


def nutrition_agent(user_data: UserInput):
    """
    Flujo principal del agente:
    1. Calcula requerimientos nutricionales del usuario
    2. Carga los alimentos desde la base limpia
    3. Genera población inicial
    4. Ejecuta algoritmo genético
    5. (Futuro) Ejecuta recocido simulado
    """

    print("🔍 Iniciando agente de búsqueda nutricional...")

    # ----------------------------------------------------
    # 1. REQUERIMIENTOS NUTRICIONALES
    # ----------------------------------------------------
    print("📌 Calculando requerimientos del usuario...")
    requirements = calculate_user_requirements(user_data)

    # ----------------------------------------------------
    # 2. CARGA DE ALIMENTOS
    # ----------------------------------------------------
    print("📌 Cargando alimentos desde la base limpia...")
    foods = get_foods()

    if not foods:
        return {
            "status": "error",
            "message": "No se pudieron cargar los alimentos desde el CSV.",
        }

    foods_dict = {item["id"]: item for item in foods}

    print(f"📌 {len(foods)} alimentos cargados correctamente.")

    # ----------------------------------------------------
    # 3. GENERACIÓN DE POBLACIÓN INICIAL
    # ----------------------------------------------------
    print("🧬 Generando población inicial...")
    population = generate_initial_population(
        foods=foods,
        user=user_data,
        requirements=requirements,
        size=200
    )

    print(f"🧬 Población inicial generada: {len(population)} individuos")

    # ----------------------------------------------------
    # 4. ALGORITMO GENÉTICO
    # ----------------------------------------------------
    print("🧪 Ejecutando algoritmo genético...")

    best_genetic = genetic_algorithm(
        population=population,
        foods_dict=foods_dict,
        user=user_data,
        requirements=requirements,
        generations=60,
        mutation_rate=0.05,
        top_k=5
    )

    print("🧬 Mejores dietas generadas (para recocido):")
    for i, d in enumerate(best_genetic, 1):
        print(f"   GA Top {i}: {d}")

    # ----------------------------------------------------
    # 5. RECOCIDO SIMULADO (cuando lo implementemos)
    # ----------------------------------------------------
    # print("🔥 Ejecutando recocido simulado...")
    # best_final = simulated_annealing(best_genetic, ...)
    best_final = best_genetic  # temporal

    # ----------------------------------------------------
    # 6. RESPUESTA FINAL
    # ----------------------------------------------------
    print("📦 Construyendo respuesta final...")

    return {
        "status": "ok",
        "message": "Agente ejecutado correctamente.",
        "requirements": requirements,
        "foods_count": len(foods),
        "best_genetic": best_genetic,
        "best_final": best_final
    }
