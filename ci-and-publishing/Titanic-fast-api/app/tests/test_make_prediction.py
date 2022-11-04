import numpy as np
import pandas as pd
from fastapi.testclient import TestClient


def test_make_prediction(client: TestClient, load_data: pd.DataFrame) -> None:
    payload = {"inputs": load_data.replace({np.nan: None}).to_dict(orient="records")}
    response = client.post(url="http://localhost:8000/api/v1/predict", json=payload)

    assert response.status_code == 200
    response = response.json()
    assert isinstance(response["predictions"][0], int)
    assert response["errors"] is None
