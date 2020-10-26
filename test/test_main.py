from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_read_model_alexnet():
    response = client.get("/model/alexnet")
    assert response.status_code == 200
    assert response.json() == {"model_name": "alexnet",
                               "message": "Deep Learning FTW!"}


def test_read_model_resnet():
    response = client.get("/model/resnet")
    assert response.status_code == 200
    assert response.json() == {"model_name": "resnet",
                               "message": "Have some residuals"}


def test_read_model_lenet():
    response = client.get("/model/lenet")
    assert response.status_code == 200
    assert response.json() == {"model_name": "lenet",
                               "message": "LeCNN all the images"}
