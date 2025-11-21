
import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "clean" / "merged_clean.csv"


def load_food_dataset():
    print("[data_loader] Cargando archivo limpio:", DATA_PATH)

    try:
        df = pd.read_csv(DATA_PATH)
        return df
    except Exception as e:
        print("ERROR al leer dataset limpio:", e)
        return pd.DataFrame()


# ================================================================
#  FILTRO CENTRAL DE RESTRICCIONES
# ================================================================

import pandas as pd

def apply_restrictions(df, user):
    """
    Aplica TODAS las restricciones del usuario:
    - vegano
    - alergias
    - diabetes (suave: no elimina alimentos, solo evita extremos)
    - hipertensión
    """

    print("[data_loader] Aplicando restricciones del usuario...")

    # ============================================================
    # 1. VEGANO  eliminar alimentos de origen animal
    # ============================================================
    if user.condition == "vegan":
        if "origen" in df.columns:
            df = df[df["origen"] != "animal"]

    # ============================================================
    # 2. ALERGIAS  eliminar alimentos cuyo nombre coincida
    # ============================================================
    if user.allergies:
        for allergen in user.allergies:
            df = df[~df["name"].str.contains(allergen, case=False, na=False)]

    # ============================================================
    # 3. DIABETES  no eliminamos alimentos, pero sí filtramos extremos
    # ============================================================
    if user.condition == "diabetes":
        if "carbs" in df.columns:
            # Limitar alimentos con > 80 g de carbohidratos por porción
            # (umbral razonable para evitar valores absurdamente altos)
            df = df[df["carbs"] <= 80]


    # ============================================================
    # 4. HIPERTENSIÓN  filtrar alimentos altos en sodio
    # ============================================================
    if user.condition == "hypertension":
        if "sodium" in df.columns:
            # límite suave por porción para evitar valores muy altos
            df = df[df["sodium"] <= 400]  # mg

    return df



# ================================================================
#  FUNCIÓN PRINCIPAL PARA EL AGENTE
# ================================================================
def get_foods(user=None):
    """
    Carga alimentos y aplica restricciones solo si se pasa user.
    """
    df = load_food_dataset()

    if df.empty:
        return []

    if user:
        df = apply_restrictions(df, user)

    return df.to_dict(orient="records")
