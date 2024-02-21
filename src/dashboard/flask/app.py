#   Created by Lachlan Doak on 15/1/24
#
#   mysqlclient is included via reqs.txt -> was needed for config

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from collections import defaultdict

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://pfs_user:pfs_secret_pw@pfs_db:3306/pfs_stats'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class main(db.Model):
    '''
    Class representing the main table in the database.

    Attributes:
        id (db.Column): Identifier column.
        item_source (db.Column): Source of the item.
        time_sent (db.Column): Timestamp of when the item was sent (primary key).
        item_key (db.Column): Key of the item.
        item_val (db.Column): Value of the item.
    '''

    id = db.Column(db.Text)
    item_source = db.Column(db.String(255))
    time_sent = db.Column(db.DateTime, primary_key=True)
    item_key = db.Column(db.String(255))
    item_val = db.Column(db.Text)
    
@app.route('/')
def index():
    '''
    Route to display a welcome message.

    Returns:
        str: Welcome message.
    '''
    return "Welcome to the Phishing For Scams Backend!"

@app.route('/data', methods=["GET"])
def get_data():
    '''
    Route to retrieve all data from the main table.

    Returns:
        Response: JSON response containing the retrieved data.
    '''
    data = main.query.all()
    formatted_data = []

    for entry in data:
        formatted_entry = {
            "identifier": entry.id,
            "source": entry.item_source,
            "timestamp": entry.time_sent,
            "purpose": entry.item_key,
            "value": entry.item_val
        }
        formatted_data.append(formatted_entry)

    return jsonify(formatted_data)

@app.route('/usage/today', methods=["GET"])
def get_today_data():
    '''
    Route to retrieve usage data for today.

    Returns:
        Response: JSON response containing the count of usage data for today.
    '''
    today = datetime.now().date()
    data = main.query.filter(main.time_sent >= today).filter(main.item_source == "scanner").all()
    count = { "count": len(data) }

    return jsonify(count)

@app.route('/usage/last-week', methods=["GET"])
def get_last_week_data():
    '''
    Route to retrieve usage data for the last week.

    Returns:
        Response: JSON response containing the processed usage data for the last week.
    '''
    start_date = datetime.now() - timedelta(days=7)
    data = main.query.filter(main.time_sent >= start_date).all()

    processed_data = {"labels": ["M", "T", "W", "T", "F", "S", "S"], "datasets": {"label": "Times Used", "data": [0, 0, 0, 0, 0, 0, 0]}}

    for entry in data:
        day_of_week = entry.time_sent.weekday()
        processed_data["datasets"]["data"][day_of_week] += 1

    return jsonify(processed_data)

@app.route('/usage/all-time', methods=["GET"])
def get_all_time_data():
    '''
    Route to retrieve usage data for all time.

    Returns:
        Response: JSON response containing the count of usage data for all time.
    '''
    data = main.query.filter(main.item_source == "scanner").all()
    count = { "count": len(data) }

    return jsonify(count)

@app.route('/scams/today', methods=["GET"])
def get_today_yesterday_data():
    '''
    Route to retrieve scam data for today.

    Returns:
        Response: JSON response containing the count of scam data for today.
    '''
    today = datetime.now().date()
    data_today = main.query.filter(main.time_sent >= today).filter(main.item_val == "SCAM").all()
    count_today = len(data_today)
    data = { "count": count_today }

    return jsonify(data)

@app.route('/scams/all-time', methods=["GET"])
def get_scams_alltime_data():
    '''
    Route to retrieve scam data for all time.

    Returns:
        Response: JSON response containing the processed scam data for all time.
    '''
    start_date = datetime.now() - timedelta(days=365)
    data = main.query.filter(main.time_sent >= start_date).all()
    scams_count_by_month = defaultdict(int)

    for entry in data:
        month_year_key = entry.time_sent.strftime("%b %Y")
        if entry.item_val == "SCAM":
            scams_count_by_month[month_year_key] += 1

    labels = []
    scam_counts = []

    for i in range(12):
        month = (datetime.now() - timedelta(days=30 * i)).strftime("%b %Y")
        labels.insert(0, month)
        scam_counts.insert(0, scams_count_by_month[month])
    processed_data = {
        "labels": labels,
        "datasets": {"label": "Scams Detected", "data": scam_counts}
    }

    return jsonify(processed_data)

if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', debug=True)