import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_admin_unauthorized_without_token(client):
    res = client.get('/admin')
    assert res.status_code == 401
