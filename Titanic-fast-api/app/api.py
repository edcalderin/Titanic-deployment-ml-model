import json
from typing import Any
from loguru import logger
import numpy as np
import pandas as pd
from classification_model import __version__ as model_version
from classification_model.predict import make_prediction
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from app import __version__, schemas
from app.config import settings

api_router = APIRouter()


@api_router.get("/about", status_code=200, response_model=schemas.About)
def about() -> dict:
    # log here
    about = schemas.About(
        app_version=__version__,
        model_version=model_version,
        project_name=settings.PROJECT_NAME,
    )
    return about.dict()


@api_router.post("/predict", status_code=200, response_model=schemas.PredictionResult)
async def predict(input_data: schemas.MultipleTitanicDataInput) -> Any:
    logger.info(f'Making predictions on inputs: {input_data.inputs}')
    
    df_input = pd.DataFrame(jsonable_encoder(input_data.inputs))
    results = make_prediction(input_data=df_input.replace({np.nan: None}))
    if results["errors"] is not None:
        logger.warning(f'Prediction validation error: {results.get("errors")}')
        raise HTTPException(status_code=500, detail=json.loads(results["errors"]))
    
    logger.info(f'Prediction results: {results.get("predictions")}')

    return results
