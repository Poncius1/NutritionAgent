import pandas as pd
from pathlib import Path
import re

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"
CLEAN_DIR = Path(__file__).parent.parent / "data" / "clean"
CLEAN_DIR.mkdir(exist_ok=True)

OUTPUT_CSV = CLEAN_DIR / "merged_clean.csv"

COLUMNS_MAP = {
    "alimento_id": "id",
    "alimento": "name",
    "Carbohidratos": "carbs",
    "Energía": "energy",
    "Lípidos": "fat",
    "Proteína": "protein",
    "Sodio": "sodium",
}

# Limpieza de unidades ejemplo: "5.4 g", "32 kcal"
def clean_numeric(value):
    if isinstance(value, (int, float)):
        return float(value)

    if not isinstance(value, str):
        return None

    # Extraer número con regex
    match = re.search(r"[-+]?\d*\.?\d+", value)
    if match:
        return float(match.group())
    return None


def clean_dataframe(df: pd.DataFrame):
    """Limpia columnas, valores y convierte a un formato estándar."""
    df = df.rename(columns=COLUMNS_MAP)

    # Mantener solo columnas necesarias
    columns_keep = ["id", "name", "carbs", "energy", "fat", "protein", "sodium"]
    df = df[[c for c in columns_keep if c in df.columns]]

    # Convertir columnas numéricas
    numeric_columns = ["carbs", "energy", "fat", "protein", "sodium"]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = df[col].apply(clean_numeric)

    # Quitar filas sin nombre o sin datos nutricionales
    df = df.dropna(subset=["name", "carbs", "energy", "fat", "protein"], how="any")

    return df


def run_cleaning():
    print("Buscando archivos CSV en:", RAW_DIR)

    csv_files = list(RAW_DIR.glob("*.csv"))

    if not csv_files:
        print("No se encontraron archivos CSV en /data/raw/")
        return

    cleaned_frames = []

    for csv in csv_files:
        print(f"Limpiando archivo: {csv.name}")
        df = pd.read_csv(csv)
        df_clean = clean_dataframe(df)
        cleaned_frames.append(df_clean)

    # Unir todo en un solo CSV limpio
    merged_df = pd.concat(cleaned_frames, ignore_index=True)
    merged_df.to_csv(OUTPUT_CSV, index=False)

    print(f"Limpieza completa. Archivo final guardado en:\n   {OUTPUT_CSV}")


if __name__ == "__main__":
    run_cleaning()
