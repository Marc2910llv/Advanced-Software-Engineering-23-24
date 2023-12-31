from flask import Flask, render_template, request, make_response, jsonify
import requests

app = Flask(__name__, instance_relative_config=True)

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        return make_response(jsonify(s=a+b), 200) # HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) # HTTP 400 BAD REQUEST

@app.route('/sub')
def sub():
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    return make_response(jsonify(s=a-b), 200)

@app.route('/mul')
def mul():
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    return make_response(jsonify(s=a*b), 200)

@app.route('/div')
def div():
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    if b == 0:
        return make_response('Cannot divide by zero\n', 400)
    else:
        return make_response(jsonify(s=a/b), 200)

@app.route('/mod')
def mod():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    if b == 0:
        return make_response('Cannot mod by zero\n', 400)
    else:
        return make_response(jsonify(s=a%b), 200)

def create_app():
    return app