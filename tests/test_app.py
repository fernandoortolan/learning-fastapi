from http import HTTPStatus

from fastapi.testclient import TestClient

from learning_fastapi.app import app


def test_root_should_return_ok_and_hello_world():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Hello, World!'}  # Assert'


def test_should_return_ok_and_html_with_hello_world():
    client = TestClient(app)  # Arrange

    response = client.get('/hello-world-with-html')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert (
        response.text
        == """
        <html>
            <head>
                <title>Hello, World!</title>
            </head>
            <body>
                <h1>Hello, World!</h1>
            </body>
        </html>"""
    )  # Assert


client = TestClient(app)
