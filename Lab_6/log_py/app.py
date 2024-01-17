from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import threading, time, os

log_db = "log_db"
user = "log"
password = os.environ.get("LOG_PASSWORD")

app = Flask(__name__, instance_relative_config=True)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{user}:{password}@{log_db}/{log_db}"

db = SQLAlchemy(app)

class Log(db.Model):
    time = db.Column(db.String(200), primary_key = True)
    log = db.Column(db.String(200), primary_key = True)

    def __init__(self, time, log):
        self.time = time
        self.log = log

with app.app_context():
    # retry, it is very slow to init the mysql db
    for i in range(100):
        try:
            db.create_all()
            print("created tables")
            break
        except:
            time.sleep(5)

@app.route('/getLogs')
def getLogs():
    res = {}
    with app.app_context():
        logs = db.session.query(Log).all()
        if logs is None:
            return {}
        for log in logs:
            res[log.time] = log.log
    return make_response(jsonify(res), 200)

@app.route('/addLog', methods=['POST'])
def addLog():
    payload = request.json
    key = payload["time"]
    value = payload["log"]
    with app.app_context():
        query = text('SELECT * FROM log WHERE log = :value AND time = :key')
        log = db.session.execute(query, {'value': value, 'key': key}).first()
        if log is None:
        # Handle the case when log is not found

            db.session.add(Log(key, value))
            db.session.commit()
        else:
            # print also log
            return make_response(jsonify(error="log already exists", log=log), 400)
    return make_response(jsonify('ok'),200)

@app.route('/countLogs/<URL>')
def countLogs(URL):
    # count the number of logs that contain the URL string at the end
    with app.app_context():
        query = text('SELECT COUNT(*) FROM log WHERE RIGHT(log, :length) = :url')
        num = db.session.execute(query, {'length': len(URL), 'url': URL}).scalar()

    return make_response(jsonify(num), 200)


def create_app():
    return app

@app.route('/crash')
def crash():
    def close():
        time.sleep(1)
        os._exit(0)
    thread = threading.Thread(target=close)
    thread.start()
    ret = str(request.host) + " crashed"
    return make_response(jsonify(s=ret), 200)