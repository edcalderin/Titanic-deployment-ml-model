import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from loguru import logger

from app.api import api_router
from app.config import settings, setup_and_logging

app = FastAPI()

root_router = APIRouter()

setup_and_logging(settings)


@root_router.get("/")
def index() -> HTMLResponse:
    body = (
        "<html>"
        "<body>"
        "<h1>Welcome to Titanic Prediction API</h1>"
        '<div>Check the docs <a href="/docs">here.</a></div>'
        "</body>"
        "</html>"
    )
    return HTMLResponse(body)


app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)
# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

if __name__ == "__main__":
    logger.debug("Debugging from Developing mode")
    uvicorn.run(app, host="localhost", port=8081, log_level="debug")
