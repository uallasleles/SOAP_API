# encoding: utf8

import json
from flask import Flask, make_response, current_app, render_template


app = Flask(__name__)
app.config.from_object('settings')


@app.route('/')
def index():
    '''index
    '''
    return render_template("index.html")


@app.route('/hello')
def hello():
    '''Visualização da API Flask de amostra que retorna JSON com alguns dados da configuração.
    '''

    response = make_response(json.dumps({
        'hello': current_app.config['HELLO'],
    }))
    response.headers['Content-Type'] = 'application/json'
    return response