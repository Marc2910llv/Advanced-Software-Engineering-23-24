from flask import Flask, request, make_response, jsonify
import requests
from requests.exceptions import ConnectionError, HTTPError
from datetime import date
import random

BACKEND_URL = 'http://backend:8000'

app = Flask(__name__, instance_relative_config=True)

def create_secret(X,response):
    example = date.today()
    value = random.randint(0,X)
    response.headers['secret'] = example.strftime("%Y")+example.strftime("%m")+example.strftime("%d")
    response.set_cookie('secret', str(4*(value+6)/2-value*2)+"a")
    return response

@app.route('/secret', methods=['GET'])
def get_secret():
    X = request.args.get('X', type = int)
    response = make_response(jsonify(secret=X), 200)
    return create_secret(X,response)

def create_app():
    return app

@app.route('/<op>', methods=['GET'])
def operation(op):
    if op not in ['add', 'sub']:
        return make_response('Invalid operation\n', 404)
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    try:
        URL = BACKEND_URL + f'/{op}?a={a}&b={b}'
        x = requests.get(URL, timeout=1)
        x.raise_for_status()
        res = x.json()
    except ConnectionError:
        return make_response('Backend service is down\n', 400)
    except HTTPError:
        return make_response('Invalid input\n', 400)
    return res