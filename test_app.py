from app import app

def test_hello():
    client = app.test.client()
    response = client.get('/')
    assert response.status.code == 200
    assert b"Hello from Jenkins MUltibranch Pipeline!" in response.data
    