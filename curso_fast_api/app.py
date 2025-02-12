from http import HTTPStatus

from fastapi.responses import HTMLResponse

from fastapi import FastAPI

from curso_fast_api.schemas import Message

app = FastAPI()

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}

@app.get('/exercicio-html', response_class=HTMLResponse)
def exercicio_aula02():
    return """  
        <html>
            <head>
                <title>Nosso olá mundo!</title>
            </head>
            <body>
                <h1> Olá Mundo </h1>
            </body>
        </html>
        """