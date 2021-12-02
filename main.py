import sys
from flask import Flask, jsonify, make_response
from flask.templating import render_template
from flask_restful import Api, Resource
from schedule import Schedule

app = Flask(__name__)

api = Api(app)

schedule = Schedule()
schedules = schedule.getSchedule()

@app.route('/', methods=['GET'])
def home():
    return schedule.getSchedule()
    
@app.route('/test')
def test():
    return {"test" : ["this", "is", "a", "test"]}

@app.route('/api/schedule', methods=['GET'])
def api():
    return jsonify(schedules)

if __name__ == '__main__':
    app.run(debug=True)
