from pydantic import BaseModel

class About(BaseModel):
    model_version: str
    app_version: str
    project_name: str