from flask import Flask, request, make_response, jsonify
from random import randrange

app = Flask(__name__, instance_relative_config=True)


def create_app():
    return app

@app.route('/concat')
def concat():
    a = request.args.get('a', type=str)
    b = request.args.get('b', type=str)
    if a and b:
        return make_response(jsonify(s=a+b), 200) # HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) # HTTP 400 BAD REQUEST

@app.route('/upper')
def upper():
    a = request.args.get('a', 0, type=str)
    return make_response(jsonify(s=a.upper()), 200)

@app.route('/lower')
def lower():
    a = request.args.get('a', 0, type=str)
    return make_response(jsonify(s=a.lower()), 200)

@app.route('/middle')
def middle():
    random = randrange(10)
    if random < 5:
        return make_response(jsonify(s=0), 200)
    else:
        return make_response(jsonify(s=1), 400)
