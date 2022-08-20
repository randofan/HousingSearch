from flask import Flask, request, jsonify
import json
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import House, Filters, db
from housingsearch import search_all


### DO NOT RUN!!! OR ELSE CRAIGSLIST AND ZILLOW WILL BAN YOUR IP ###
@app.route('/', methods=['GET'])
def index():
    houses = []
    if request.args:
        houses: list[House] = search_all(Filters(**request.args))
        try:
            db.session.add_all(houses)
            db.session.commit()
            return jsonify(House.query.filter_by(**request.args).all())
        except:
            return 'Oopsie Daisy'
        
    # return json.dumps([House('1234 Test Ln', 420, 1,1, 4200, 'https://www.google.com', 'https://image.com', {'latitude': 2000, 'longitude': 1000},
    #                 1, datetime.now(), True, True, False, True, True, False, False)])



if __name__ == '__main__':    
    app.run(debug=True)
    # house = House(address='1234 Test Ln', price=420, beds=1,baths=1, area=4200, url='https://www.google.com', image='https://image.com', 
    #                         coords={'latitude': 2000, 'longitude': 1000}, id=1, date=datetime.now(), cats=True, dogs=True, parking=False, 
    #                         laundry=True, apartment=True, townhouse=False, house=False)
    # print(jsonify(house))