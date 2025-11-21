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
# IMPORTS DEL AGENTE COMPLETO
# ============================================================
from models.user_input import UserInput
from services.agent_manager import nutrition_agent
from services.data_loader import load_food_dataset


# ============================================================
# Ejecutar limpieza si existe
# ============================================================
CLEAN_SCRIPT = Path(__file__).parent / "clean_base.py"

def try_run_cleaner():
    if CLEAN_SCRIPT.exists():
        print("\n🧹 Ejecutando clean_base.py para regenerar merged_clean.csv...\n")
        subprocess.run(["python", str(CLEAN_SCRIPT)], check=False)
    else:
        print("⚠ clean_base.py no encontrado. Saltando limpieza.")


# ============================================================
# TEST COMPLETO DEL AGENTE
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

    # 3. Validación rápida del CSV limpio
    foods = load_food_dataset()
    if isinstance(foods, pd.DataFrame):
        foods = foods.to_dict(orient="records")

    if not foods:
        print("❌ ERROR: merged_clean.csv no contiene datos.")
        return

    if "id" not in foods[0]:
        print("❌ ERROR: El dataset limpio NO incluye columna 'id'.")
        print("Columnas encontradas:", list(foods[0].keys()))
        return

    print(f"✔ Dataset limpio OK ({len(foods)} alimentos)\n")

    # ============================================================
    # 4. Ejecutar el agente completo
    # ============================================================
    print("🚀 Ejecutando nutrition_agent...\n")

    result = nutrition_agent(user)

    print("\n==============================")
    print("📦 RESULTADO FINAL DEL AGENTE")
    print("==============================\n")

    print("Estado:", result.get("status"))
    print("Mensaje:", result.get("message"))

    print("\n📌 Requerimientos calculados:")
    print(result.get("requirements", {}))

    print("\n🥗 Dietas propuestas por el GA:")
    best_genetic = result.get("best_genetic", [])
    for i, d in enumerate(best_genetic, 1):
        print(f"GA {i}:", d)

    print("\n🔥 Dieta final (post-recocido simulado):")
    print(result.get("best_final"))

    print("\n==============================")
    print("📦 TEST COMPLETO FINALIZADO")
    print("==============================\n")


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    run_full_test()
