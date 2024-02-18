# mysqlclient

from flask import Flask, jsonify, request, abort, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy, func
from datetime import datetime, timedelta

app = Flask(__name__)

#mysql://username:password@host:port/database_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://pfs_user:pfs_secret_pw@pfs_db:3306/pfs_stats'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class main(db.Model):
    id = db.Column(db.Text)
    item_source = db.Column(db.String(255))
    time_sent = db.Column(db.DateTime, primary_key=True)
    item_key = db.Column(db.String(255))
    item_val = db.Column(db.Text)

    #def __repr__(self):
        #return f'<Email Id: {self.id}>'
    
@app.route('/')
def index():
    data = main.query.all()
    #return render_template('index.html', instances=data)
    return "Welcome to the Phishing For Scams Backend!"

@app.route('/data', methods=["GET"])
def get_data():
    data = main.query.all()
    return render_template('index.html', instances=data)
    #return jsonify(data)

@app.route('/data/id/<string:id>', methods=["GET"])
def get_data_by_id(id):
    data = main.query.filter(main.id == id).all()
    if not data:
        abort(404)
    return render_template('index.html', instances=data)
    #return jsonify(data)

@app.route('/data/source/<string:item_source>')
def get_data_by_source(item_source):
    data = main.query.filter(main.item_source == item_source).all()
    if not data:
        abort(404)
    return render_template('index.html', instances=data)
    #return jsonify(data)

@app.route('/data/time/<string:time_sent>')
def get_data_by_time(time_sent):
    try:
        time_sent_datetime = datetime.fromisoformat(time_sent)
    except ValueError:
        abort(400, "Invalid datetime format")
    data = main.query.filter(main.time_sent == time_sent_datetime).all()
    if not data:
        abort(404)
    return render_template('index.html', instances=data)
    #return jsonify(data)

@app.route('/data/key/<string:item_key>')
def get_data_by_key(item_key):
    data = main.query.filter(main.item_key == item_key).all()
    if not data:
        abort(404)
    return render_template('index.html', instances=data)
    #return jsonify(data)

@app.route('/data/val/<string:item_val>')
def get_data_by_value(item_val):
    data = main.query.filter(main.item_val == item_val).all()
    if not data:
        abort(404)
    return render_template('index.html', instances=data)
    #return jsonify(data)

@app.route('/data/last-week', methods=["GET"])
def get_last_week_data():
    start_date = datetime.now() - timedelta(days=7)
    data = db.session.query(main.time_sent, func.count()).filter(main.time_sent >= start_date).group_by(main.time_sent).all()
    processed_data = {"labels": ["M", "T", "W", "T", "F", "S", "S"], "datasets": {"label": "Sales", "data": [0, 0, 0, 0, 0, 0, 0]}}

    for row in data:
        day_of_week = row[0].weekday()  # Get the day of the week (0 = Monday, 1 = Tuesday, ...)
        processed_data["datasets"]["data"][day_of_week] += row[1]  # Increment the count for the corresponding day

    return jsonify(processed_data)

if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', debug=True)