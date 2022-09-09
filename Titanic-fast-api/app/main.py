import uvicorn
from fastapi import APIRouter, FastAPI

from app.api import api_router

app = FastAPI()

root_router = APIRouter()


@root_router.get("/")
def root():
    return {"message": "welcome"}


app.include_router(api_router)
app.include_router(root_router)

if __name__ == "__main__":
    uvicorn.run(app, log_level="debug")
