from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from learning_fastapi.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello, World!'}


@app.get(
    '/hello-world-with-html',
    status_code=HTTPStatus.OK,
    response_class=HTMLResponse,
)
def read_route_hello_world_with_html():
    return """
        <html>
            <head>
                <title>Hello, World!</title>
            </head>
            <body>
                <h1>Hello, World!</h1>
            </body>
        </html>"""
