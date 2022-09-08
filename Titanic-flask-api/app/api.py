from fastapi import APIRouter
'''from classification_model.predict import make_predictions'''
from classification_model import __version__ as model_version
from app import __version__, schemas, config

api_router = APIRouter()

@api_router.get('/about', status_code=200, response_model=schemas.About)
def about() -> dict:
    about = schemas.About(
        app_version=__version__,
        model_version='model_version',
        project_name=config.PROJECT_NAME
    )
    return about.dict()

'''@api_router.post('/about', status_code=200, response_model={})
def predict() -> Any:
    make_predictions()'''