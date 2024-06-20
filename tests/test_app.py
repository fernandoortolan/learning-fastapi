from http import HTTPStatus

from fastapi.testclient import TestClient

from learning_fastapi.app import app


def test_root_should_return_ok_and_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'sarah',
            'email': 'sarah@example.com',
            'password': 'action',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'sarah',
        'email': 'sarah@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'sarah',
                'email': 'sarah@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'sarah',
            'email': 'sarah@example.com',
            'password': 'banana',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'sarah',
        'email': 'sarah@example.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


# def test_should_return_ok_and_html_with_hello_world():
#     client = TestClient(app)  # Arrange

#     response = client.get('/hello-world-with-html')  # Act

#     assert response.status_code == HTTPStatus.OK  # Assert
#     assert (
#         response.text
#         == """
#         <html>
#             <head>
#                 <title>Hello, World!</title>
#             </head>
#             <body>
#                 <h1>Hello, World!</h1>
#             </body>
#         </html>"""
#     )  # Assert


client = TestClient(app)
