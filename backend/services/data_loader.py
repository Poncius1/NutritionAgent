import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "clean" / "merged_clean.csv"

def load_food_dataset():
    """
    Carga el archivo limpio generado por clean_base.py.
    Devuelve una lista de diccionarios lista para usar.
    """
    print("[data_loader] Cargando archivo:", DATA_PATH)

    try:
        df = pd.read_csv(DATA_PATH)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        print("ERROR: No existe merged_clean.csv — ejecuta clean_base.py")
        return []
    except Exception as e:
        print("ERROR al leer dataset limpio:", e)
        return []


def get_foods():
    """Devuelve todos los alimentos."""
    print("[data_loader] get_foods() llamado")
    return load_food_dataset()


def get_foods_filtered(min_protein=None, max_carbs=None):
    """
    Filtrado básico usando el dataset limpio.
    """
    print("[data_loader] get_foods_filtered() llamado")

    foods = load_food_dataset()
    df = pd.DataFrame(foods)

    if min_protein:
        df = df[df["protein"] >= min_protein]
    if max_carbs:
        df = df[df["carbs"] <= max_carbs]
 

    return df.to_dict(orient="records")
