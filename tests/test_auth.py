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

def test_register_and_login(client):
    res_reg = client.post('/register', json={"username": "testuser", "password": "Password123!"})
    assert res_reg.status_code == 201

    res_login = client.post('/login', json={"username": "testuser", "password": "Password123!"})
    assert res_login.status_code == 200
    assert "token" in res_login.get_json()
