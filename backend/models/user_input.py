
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class UserInput(BaseModel):
    name: str
    age: int = Field(..., ge=10, le=120)
    sex: Literal["male", "female"]
    weight: float = Field(..., gt=0)
    height: float = Field(..., gt=0)

    fat_percentage: Optional[float] = Field(None, ge=1, le=60)

    exercise: Literal["0-1", "2-3", "4-5", "6-7", "extreme"] = "0-1"

    condition: Literal["none", "diabetes", "hypertension", "vegan"] = "none"
    allergies: List[str] = []

    

    class Config:
        schema_extra = {
            "example": {
                "name": "Ángel",
                "age": 22,
                "sex": "male",
                "weight": 70.0,
                "height": 175.0,
                "fat_percentage": 18.0,
                "exercise": "2-3",
                "condition": "diabetes",
                "allergies": ["fresa", "maní"],
            }
        }
