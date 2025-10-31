from fastapi import APIRouter

router = APIRouter()

# ===============================
#  Endpoints 
# ===============================

@router.get("/foods")
def list_foods():
    print("[GET] /diet/foods fue llamado")
    return {"message": "GET /diet/foods funcionando correctamente"}


@router.get("/foods/filter")
def filter_foods():
    print("[GET] /diet/foods/filter fue llamado")
    return {"message": "GET /diet/foods/filter funcionando correctamente"}


@router.post("/requirements")
def get_user_requirements():
    print("[POST] /diet/requirements fue llamado")
    return {"message": "POST /diet/requirements funcionando correctamente"}


@router.post("/generate")
def generate_regimen():
    print("[POST] /diet/generate fue llamado")
    return {"message": "POST /diet/generate funcionando correctamente"}
