import pytest
from app import create_app
from app.database import init_db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    init_db()
    with app.test_client() as client:
        yield client

def test_sqli_attempt_blocked(client):
    sqli_payload = "' OR '1'='1"
    res = client.post('/login', json={"username": sqli_payload, "password": "anything"})
    assert res.status_code == 401
