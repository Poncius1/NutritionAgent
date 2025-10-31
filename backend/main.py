import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes_diet import router as diet_router



app = FastAPI(
    title="Nutrition AI Agent API",
    description=(
        "API para generar dietas personalizadas con algoritmos evolutivos y "
        "recocido simulado, basada en la Canasta Regional del Bien Comer (CONABIO)."
    )
)


app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(diet_router,prefix="/diet")