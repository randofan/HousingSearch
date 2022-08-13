from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from utils import House, Filters
from dacite import from_dict
from housingsearch import search_all


app = Flask(__name__)

# TODO db caching to limit number of requests
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

# class Todo(db.Model):
#     address = db.Column(db.String(100), primary_key=True)
#     price = db.Column(db.Integer, nullable=False)
#     beds = db.Column(db.Integer, nullable=False)
#     baths = db.Column(db.Integer, nullable=False)
#     area = db.Column(db.Integer, nullable=False)
#     url = db.Column(db.String(100), nullable=False)
#     image = db.Column(db.String(100), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<Task %r>' % self.address



### DO NOT RUN!!! OR ELSE CRAIGSLIST AND ZILLOW WILL BAN YOUR IP ###
@app.route('/', methods=['GET'])
def index():
    houses = []
    if request.args:
        filters: Filters = from_dict(request.args)
        houses: set[House] = search_all(filters)
    return render_template('index.html', houses=houses)

@app.route('/update', methods=['POST'])
def update():
    pass

if __name__ == '__main__':
    app.run(debug=True)