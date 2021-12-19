from flask import Flask, jsonify
from schedule import Schedule
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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