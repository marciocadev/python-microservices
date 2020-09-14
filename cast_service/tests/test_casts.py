import json

import pytest

from app.api import db_manager


def test_create_cast(test_app, monkeypatch):
    test_request_payload = { "name": "string", "nationality": "string" }
    test_response_payload = { "name": "string", "nationality": "string", "id": 2 }

    async def mock_post(payload):
        return 2

    monkeypatch.setattr(db_manager, "add_cast", mock_post)

    response = test_app.post("/api/v1/casts/", data = json.dumps(test_request_payload))

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_read_cast(test_app, monkeypatch):
    test_data = {"id": 1, "name": "string", "nationality": "string" }

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(db_manager, "get_cast", mock_get)

    response = test_app.get("/api/v1/casts/1")
    assert response.status_code == 200
    assert response.json() == test_data


def test_read_cast_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(db_manager, "get_cast", mock_get)

    response = test_app.get("/api/v1/casts/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Cast not found"


#def test_create_cast_invalid_json(test_app):
#    test_request_payload = { "name": "string" }
#
#    response = test_app.post("/api/v1/casts/", data = json.dumps(test_request_payload))
#    assert response.status_code == 422