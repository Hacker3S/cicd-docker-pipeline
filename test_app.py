import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_status_ok(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == 'running'


def test_health_status_ok(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'
    assert 'timestamp' in response.json


def test_info_returns_app_metadata(client):
    response = client.get('/api/info')
    assert response.status_code == 200
    assert response.json['app'] == 'cicd-docker-pipeline'


def test_unknown_route_returns_404(client):
    response = client.get('/this-route-does-not-exist')
    assert response.status_code == 404
