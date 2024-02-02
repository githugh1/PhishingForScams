# mysqlclient

from flask import Flask, jsonify, request, abort, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime

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

@app.route('/data/<string:id>', methods=["GET"])
def get_data_by_id(id):
    data = main.query.filter(main.id == id).all()
    if data is None:
        abort(404)
    return render_template('index.html', instances=data)
    #return jsonify(data)

if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', debug=True)