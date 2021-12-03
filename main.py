import sys
from flask import Flask, json, jsonify, make_response
#from flask.templating import render_template
from flask_restful import Api, Resource
from schedule import Schedule

app = Flask(__name__)

api = Api(app)

schedule = Schedule()


@app.route('/', methods=['GET'])
def home():
    return schedule.getToday("20211203")


@app.route('/api/schedule', methods=['GET'])
def scheduleApi():
    return jsonify(schedule.getSchedule())


@app.route('/api/agenda/<date>', methods=['GET'])
def agendaAPI(date):
    return jsonify(schedule.getToday(date))


if __name__ == '__main__':
    app.run(debug=True)
