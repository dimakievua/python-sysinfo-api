from sysinfo import create_app
import json

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/healthcheck')
    assert response.data == b'Ok'


def test_hello(client):
    response = client.get('/api/all')
    response = json.loads(response.data)
    assert response['Status'] == 'SUCCESS'
