from flask import Flask, request, make_response, jsonify
from datetime import date

app = Flask(__name__, instance_relative_config=True)

@app.route('/example')
def example():
    a = request.args.get('a',type=float)
    example = date.today()
    d1 = example.strftime("%d")
    d2 = example.strftime("%m")
    response = make_response(jsonify(s=a), 200)
    response.headers['Solution'] = d1 + d2
    return response

@app.route('/ex1')
def ex1():
    a = request.args.get('X',type=str)

    if not a:
        return make_response('Invalid input\n', 400)  # HTTP 400 BAD REQUEST

    digit = 0
    character = 0
    for c in a:
        if c.isdigit():
            digit += 1
        elif c.isalpha():
            character += 1
    
    if digit < 1 or character < 1:
        return make_response('Operation cannot be performed\n', 400) # HTTP 400 BAD REQUEST

    result = digit / character
    return make_response(jsonify({'s': result}), 200) # HTTP 200 OK

def create_app():
    return app
