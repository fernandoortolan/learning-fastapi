from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from learning_fastapi.schemas import (
    Message,
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()

database = []
auto_increment = 0


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello, World!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    global auto_increment
    auto_increment += 1

    user_with_id = UserDB(**user.model_dump(), id=auto_increment)

    database.append(user_with_id)

    return user_with_id


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.get('/users/{user_id}', response_model=UserPublic)
def read_user(user_id: int):
    id_list = []
    for userdb in database:
        id_list.append(userdb.id)

    if user_id not in id_list:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    index = id_list.index(user_id)
    user = database[index]

    return user


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    id_list = []
    for userdb in database:
        id_list.append(userdb.id)

    if user_id not in id_list:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    user_with_id = UserDB(**user.model_dump(), id=user_id)

    index = id_list.index(user_id)
    database[index] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    id_list = []
    for userdb in database:
        id_list.append(userdb.id)

    if user_id not in id_list:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    index = id_list.index(user_id)
    del database[index]

    return {'message': 'User deleted'}
