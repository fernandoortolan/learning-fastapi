from http import HTTPStatus

from learning_fastapi.schemas import UserPublic


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


def test_create_user_username_already_exists_exception(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'test',
            'email': 'user@example.com',
            'password': 'mypassword',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Username already exists'}


def test_create_user_email_already_exists_exception(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'bob',
            'email': 'test@example.com',
            'password': 'mypassword',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Email already exists'}


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_read_user(client, user):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'test',
        'email': 'test@example.com',
        'id': 1,
    }


def test_read_user_not_found_exception(client, user):
    response = client.get('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'sarah22',
            'email': 'sarah@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'sarah22',
        'email': 'sarah@example.com',
        'id': 1,
    }


def test_update_user_not_found_exception(client, user):
    response = client.put(
        '/users/2',
        json={
            'username': 'sarah22',
            'email': 'sarah@example.com',
            'password': 'blackforest',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client, user):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found_exception(client, user):
    response = client.delete('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
