from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class UserInput(BaseModel):
    nombre: str = Field(..., description="Nombre del usuario")
    edad: int = Field(..., description="Edad en años")
    sexo: Literal["masculino", "femenino", "otro"] = Field(..., description="Sexo del usuario")
    peso: float = Field(..., description="Peso en kilogramos (kg)")

    porcentaje_musculo: Optional[float] = Field(None, description="Porcentaje de masa muscular (opcional)")
    porcentaje_grasa: Optional[float] = Field(None, description="Porcentaje de grasa corporal (opcional)")

    alergias: Optional[List[str]] = Field(None, description="Lista de alergias alimenticias (opcional)")
    condiciones: Optional[List[str]] = Field(None, description="Condiciones médicas relevantes (opcional)")

    ejercicio: Optional[Literal[
        "menos de 1 vez por semana",
        "2-3 veces por semana",
        "5 o más días por semana"
    ]] = Field(None, description="Frecuencia de ejercicio físico")

    agua_litros: Optional[float] = Field(None, description="Cantidad de agua consumida al día (litros)")

    
