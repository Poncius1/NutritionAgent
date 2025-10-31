from pathlib import Path
import pandas as pd

# Ruta al archivo CSV (no modificar)
CSV_PATH = Path(__file__).parent.parent / "data" / "Canasta.csv"


def get_all_foods():
    """
    Cargar todos los alimentos desde el archivo CSV.
    - Leer la base de datos
    - Convertir a lista de diccionarios
    """
    try:
        print(f"Cargando todos los alimentos desde: {CSV_PATH}")
        # TODO: Implementar lectura del archivo CSV con pandas.read_csv()
        return []
    except FileNotFoundError:
        print("Archivo Canasta.csv no encontrado en la ruta especificada.")
        return []
    except Exception as e:
        print(f"  Error inesperado al cargar los alimentos: {e}")
        return []


def get_filtered_foods():
    """
    Filtrar alimentos según criterios de macronutrientes.
    - max_cal: Energía máxima (kcal)
    - max_carbs: Carbohidratos máximos (g)
    - min_protein: Proteína mínima (g)
    """
    print("Filtrando alimentos con parámetros ")
        
