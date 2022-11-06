from typing import Generator

import pandas as pd
import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def load_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "pclass": [1],
            "sex": ["female"],
            "age": [29],
            "sibsp": [0],
            "parch": [0],
            "fare": [211.3375],
            "cabin": ["B5"],
            "embarked": ["S"],
            "name": ["Miss. Elisabeth Walton"],
            "ticket": ["24160"],
            "boat": [2],
            "body": [None],
            "home_dest": ["St Louis, MO"],
        }
    )


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
