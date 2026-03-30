from copy import deepcopy

import importlib
import pytest
from fastapi.testclient import TestClient

app_module = importlib.import_module("src.app")


@pytest.fixture(scope="session")
def client():
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities():
    original_activities = deepcopy(app_module.activities)
    yield
    app_module.activities = deepcopy(original_activities)
