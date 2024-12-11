from http import HTTPStatus

from fastapi.testclient import TestClient

from backend_techin.app import app

# arrange
# act
# assert


def test_read_root_deve_retornar_ok_helloworld():
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'hello world'}
