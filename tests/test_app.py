from http import HTTPStatus


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


def test_read_user(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'sarah',
        'email': 'sarah@example.com',
        'id': 1,
    }


def test_read_user_not_found_exception(client):
    response = client.get('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'sarah22',
            'email': 'sarah@example.com',
            'password': 'banana',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'sarah22',
        'email': 'sarah@example.com',
        'id': 1,
    }


def test_update_user_not_found_exception(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'sarah22',
            'email': 'sarah@example.com',
            'password': 'banana',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found_exception(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
