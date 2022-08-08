from flask import Flask, render_template, requests
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import constants


app = Flask(__name__)
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

@app.route('/', methods=['GET'])
def index():
    houses = []
    # if request.args:
    #     filters = craigslist_filters(request.args)
    #     houses.extend(list(pycraigslist.housing.apa(site="seattle", zip_code="98105", filters=filters).search()))
    return render_template('index.html', houses=houses)

@app.route('/update', methods=['POST'])
def update():
    pass

if __name__ == '__main__':
    app.run(debug=True)