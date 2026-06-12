from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_appointment_intent():

    response = client.post(
        "/api/receptionist/respond",
        json={
            "message": "I need an appointment"
        }
    )

    assert response.status_code == 200
    assert response.json()["intent"] == "appointment_booking"


def test_business_hours():

    response = client.post(
        "/api/receptionist/respond",
        json={
            "message": "What are your hours?"
        }
    )

    assert response.status_code == 200
    assert response.json()["intent"] == "business_hours"


def test_pricing_query():

    response = client.post(
        "/api/receptionist/respond",
        json={
            "message": "Tell me about your price"
        }
    )

    assert response.status_code == 200
    assert response.json()["intent"] == "pricing_query"


def test_empty_message():

    response = client.post(
        "/api/receptionist/respond",
        json={
            "message": ""
        }
    )

    assert response.status_code == 400