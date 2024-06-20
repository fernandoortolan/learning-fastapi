import pytest
from fastapi.testclient import TestClient

from learning_fastapi.app import app


@pytest.fixture()
def client():
    return TestClient(app)
