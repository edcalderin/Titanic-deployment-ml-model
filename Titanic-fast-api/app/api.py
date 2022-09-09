import json
from typing import Any

import numpy as np
import pandas as pd
from classification_model import __version__ as model_version
from classification_model.predict import make_prediction
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from app import __version__, config, schemas

api_router = APIRouter()


@api_router.get("/about", status_code=200, response_model=schemas.About)
def about() -> dict:
    # log here
    about = schemas.About(
        app_version=__version__,
        model_version=model_version,
        project_name=config.PROJECT_NAME,
    )
    return about.dict()


@api_router.post("/predict", status_code=200, response_model=schemas.PredictionResult)
def predict(input_data: schemas.MultipleTitanicDataInput) -> Any:
    # log here
    df_input = pd.DataFrame(jsonable_encoder(input_data.inputs))
    results = make_prediction(input_data=df_input.replace({np.nan: None}))
    if results["errors"] is not None:
        # log here
        raise HTTPException(status_code=500, detail=json.loads(results["errors"]))
    # log here

    return results
