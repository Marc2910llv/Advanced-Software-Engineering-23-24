import requests,time
from datetime import date

from flask import Flask, request, make_response, jsonify
from requests.exceptions import ConnectionError, HTTPError
from urls import *
import subprocess

ALLOWED_MATH_OPS = ['add', 'sub', 'mul', 'div', 'mod', 'random']
ALLOWED_STR_OPS = ['lower', 'upper', 'concat','middle']

app = Flask(__name__, instance_relative_config=True)


def create_app():
    return app

@app.route('/math/<op>')
def math(op):
    if op not in ALLOWED_MATH_OPS:
        return make_response('Invalid operation\n', 404)
    try:
        a = request.args.get('a', type=float)
        b = request.args.get('b', type=float)
        URL = MATH_URL + f'/{op}?a={a}&b={b}'
        x = requests.get(URL, timeout=1)
        x.raise_for_status()
        res = x.json()
        return res
    except (ConnectionError):
        try:
            URL = MATH_URL + f'/{op}?a={a}&b={b}'
            x = requests.get(URL, timeout=1)
            x.raise_for_status()
            res = x.json()
        except ConnectionError:
            return make_response('Math service is down\n', 404)
        except HTTPError:
            return make_response('Invalid input\n', 400)

        return res

@app.route('/str/<op>')
def string(op):
    if op not in ALLOWED_STR_OPS:
        return make_response('Invalid operation\n', 404)
    try:
        if op == 'middle':
            x = requests.get(STRING_URL + '/middle', timeout=1)
        if op == 'lower' or op == 'upper':
           a = request.args.get('a', type=str)
           x = requests.get(STRING_URL + f'/{op}?a={a}', timeout=1)
        if op == 'concat':
            a = request.args.get('a', type=str)
            b = request.args.get('b', type=str)
            x = requests.get(STRING_URL + f'/{op}?a={a}&b={b}', timeout=1)
            time.sleep(1)
        x.raise_for_status()
        return x.json()
    except ConnectionError:
        return make_response('String service is down\n', 404)
    except HTTPError:
        return make_response('Invalid input\n', 400)

    
@app.route('/secret')
def secret():
    response = make_response(jsonify(s='This is a secret'), 200)
    today = date.today()
    d1 = today.strftime("%d")
    d2 = today.strftime("%m")
    response.headers['Solution'] = d1 + d2
    return response

@app.route('/cowsay')
def bandit():
    command = "cowsay"
    arguments = ["-t","ASE"]

    # Run the command with arguments
    process = subprocess.Popen([command] + arguments, stdout=subprocess.PIPE)

    # Get the output
    output, error = process.communicate()

    if error:
        return make_response(f"An error occurred: {error}", 404)
    else:
        return make_response(jsonify(s=output.decode("utf-8")), 200)