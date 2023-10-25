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

#add other routes here
@app.route('/sub')
def subtract():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = a - b
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input'})

@app.route('/mul')
def multiply():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = a * b
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input'})

@app.route('/div')
def divide():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        if b == 0:
            return jsonify({'error': 'Division by zero is not allowed'})
        result = a / b
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input'})

@app.route('/mod')
def modulus():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        if b == 0:
            return jsonify({'error': 'Modulus by zero is not allowed'})
        result = a % b
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input'})

def create_app():
    return app