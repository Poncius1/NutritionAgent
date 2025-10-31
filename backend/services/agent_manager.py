""""
Módulo principal del agente inteligente.
Genera la búsqueda de dietas usando algoritmos genéticos y recocido simulado.
"""

from models.user_input import UserInput
from services.diet_calculation import calculate_user_requirements
from services.data_filter import get_all_foods, get_filtered_foods
from algorithms.genetic import genetic_algorithm
from algorithms.annealing import simulated_annealing


def nutrition_agent(user_data: UserInput):
    """
    Ejecuta el flujo principal del agente.
    - Calcula requerimientos nutricionales.
    - Obtiene alimentos disponibles o filtrados
    - ejecuta algoritmos de optimización.
    """
    print("Iniciando agente de búsqueda nutricional...")
    
    # Ejemplo
    print("Obteniendo requerimientos del usuario...")
    requirements = calculate_user_requirements(user_data)
    
    print("Cargando alimentos disponibles...")
    foods = get_all_foods()

    print("(Mock) Algoritmos genético y recocido.")

    
    return {
        "status": "ok",
        "message": "Agente ejecutado correctamente (versión base).",
        "requirements": requirements,
        "foods_count": len(foods) if foods else 0
    }
