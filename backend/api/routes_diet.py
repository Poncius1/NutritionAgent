from fastapi import APIRouter
from models.user_input import UserInput
from services.data_loader import get_foods
from services.diet_calculation import calculate_user_requirements
from services.agent_manager import nutrition_agent

router = APIRouter(prefix="/diet")


# =============================================================
#  Opcional: ver datos
# =============================================================
@router.get("/foods")
def list_foods():
    print("[GET] /diet/foods fue llamado")
    foods = get_foods()
    return {
        "count": len(foods),
        "foods": foods[:20]  # evitar devolver miles de filas
    }


@router.get("/foods/filter")
def filter_foods():
    print("[GET] /diet/foods/filter fue llamado")
    return {"message": "filtrado avanzado aún no implementado"}


# =============================================================
#  OPCIONAL: calcular requerimientos
# =============================================================
@router.post("/requirements")
def post_requirements(user_data: UserInput):
    print("[POST] /diet/requirements fue llamado")
    req = calculate_user_requirements(user_data)
    return {
        "status": "ok",
        "requirements": req
    }


# =============================================================
#  ENDPOINT PRINCIPAL: Generar dieta con el agente 
# =============================================================
@router.post("/generate")
def generate_regimen(user_data: UserInput):
    """
     endpoint que usa el frontend.
    Ejecuta TODO el agente de búsqueda.
    """
    print("[POST] /diet/generate fue llamado")
    
    result = nutrition_agent(user_data)

    return result
