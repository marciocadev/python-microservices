import json

import pytest

from app.api.casts import casts

def test_get(test_app, monkeypatch):
    test_data = { "name": "string", "nationality": "string", "id": 1 }

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(casts, "get", mock_get)

    response = test_app.get("/api/v1/casts/1")
    assert response.status_code == 200

