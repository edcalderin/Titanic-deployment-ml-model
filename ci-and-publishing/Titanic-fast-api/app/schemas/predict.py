from typing import Any, List, Optional

from classification_model.preprocessing.validation import TitanicInputSchema
from pydantic import BaseModel


class PredictionResult(BaseModel):
    errors: Optional[Any]
    predictions: Optional[List[int]]
    version: str


class MultipleTitanicDataInput(BaseModel):
    inputs: List[TitanicInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "pclass": 1,
                        "sex": "female",
                        "age": 29,
                        "sibsp": 0,
                        "parch": 0,
                        "fare": 211.3375,
                        "cabin": "B5",
                        "embarked": "S",
                        "name": "Miss. Elisabeth Walton",
                        "ticket": "24160",
                        "boat": 2,
                        "body": None,
                        "home_dest": "St Louis, MO",
                    }
                ]
            }
        }
