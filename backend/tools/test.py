import sys
from pathlib import Path
import subprocess
import pandas as pd

# ============================================================
# CONFIGURAR PYTHONPATH PARA IMPORTAR DESDE /backend/
# ============================================================
ROOT = Path(__file__).resolve().parent.parent   # backend/
sys.path.append(str(ROOT))

print(f"[BOOT] Agregando al PYTHONPATH: {ROOT}")

# ============================================================
#  IMPORTS DEL PROYECTO
# ============================================================
from models.user_input import UserInput
from services.data_loader import load_food_dataset
from services.diet_calculation import calculate_user_requirements
from algorithms.population import generate_initial_population
from algorithms.genetic import genetic_algorithm

# ============================================================
#  Ejecutar limpieza si existe
# ============================================================
CLEAN_SCRIPT = Path(__file__).parent / "clean_base.py"


def try_run_cleaner():
    if CLEAN_SCRIPT.exists():
        print("\n🧹 Ejecutando clean_base.py para regenerar merged_clean.csv...\n")
        subprocess.run(["python", str(CLEAN_SCRIPT)], check=False)
    else:
        print("⚠ clean_base.py no encontrado. Saltando limpieza.")


# ============================================================
#  TEST COMPLETO DEL AGENTE
# ============================================================
def run_full_test():
    print("\n==============================")
    print("🔥 INICIANDO TEST COMPLETO 🔥")
    print("==============================\n")

    # 1. Limpieza opcional
    try_run_cleaner()

    # 2. Usuario de prueba
    user = UserInput(
        name="Test User",
        age=25,
        sex="male",
        weight=70.0,
        height=175.0,
        fat_percentage=15.0,
        exercise="2-3",
        condition="none",
        allergies=[]
    )

    print(f"👤 Usuario de prueba:\n{user}\n")

    # 3. Requerimientos nutricionales
    print("📌 Calculando requerimientos...")
    requirements = calculate_user_requirements(user)
    print("✔ Requerimientos:", requirements)

    # 4. Cargar dataset limpio
    print("\n📌 Cargando alimentos limpios...")
    foods = load_food_dataset()

    # Normalizar dataset: aceptar list o DataFrame
    if isinstance(foods, pd.DataFrame):
        if foods.empty:
            print("❌ ERROR: merged_clean.csv está vacío.")
            return
        foods = foods.to_dict(orient="records")

    if not isinstance(foods, list) or len(foods) == 0:
        print("❌ ERROR: No se pudieron cargar alimentos.")
        return

    print(f"✔ {len(foods)} alimentos cargados correctamente.")

    # ============================================================
    # VALIDAR QUE EXISTE LA COLUMNA "id"
    # ============================================================
    first = foods[0]
    if "id" not in first:
        print("\n❌ ERROR: merged_clean.csv no contiene columna 'id'.")
        print("   Revisa clean_base.py o el CSV original.")
        print("   Columnas encontradas:", list(first.keys()))
        return

    # Diccionario id → alimento
    foods_dict = {f["id"]: f for f in foods}

    # 5. Generar población inicial
    print("\n🧬 Generando población inicial...")
    population = generate_initial_population(
        foods=foods,
        user=user,
        requirements=requirements,
        size=200
    )
    print(f"✔ Población inicial generada ({len(population)} individuos).")

    # 6. Ejecutar GA
    print("\n🧪 Ejecutando algoritmo genético...")
    best = genetic_algorithm(
        population=population,
        foods_dict=foods_dict,
        user=user,
        requirements=requirements,
        generations=50,
        mutation_rate=0.05,
        top_k=5
    )

    print("\n==============================")
    print("🏆 MEJORES DIETAS (GA)")
    print("==============================")

    for i, d in enumerate(best, 1):
        print(f"TOP {i}: {d}")

    print("\n==============================")
    print("📦 TEST COMPLETO FINALIZADO")
    print("==============================\n")


# ============================================================
#  MAIN
# ============================================================
if __name__ == "__main__":
    run_full_test()
