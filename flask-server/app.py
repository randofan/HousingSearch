from flask import Flask, request, Response
import json
from models import Filters
import dataclasses
from housingsearch import search_all

app = Flask(__name__)

# TODO include try-catch here for invalid inputs
@app.route('/search', methods=['GET'])
def index():
    if request.args: 
        try: return json.dumps([dataclasses.asdict(house) for house in search_all(Filters(**request.args))])
        except Exception as e: return Response("Invalid Arguments", status=400)
            
    else: return Response("Require Arguments", status=400)
    # return json.dumps([House('1234 Test Ln', 420, 1,1, 4200, 'https://www.google.com', 'https://image.com', {'latitude': 2000, 'longitude': 1000},
    #                 1, datetime.now(), True, True, False, True, True, False, False)])



if __name__ == '__main__':    
    app.run(debug=True)
    # house = House(address='1234 Test Ln', price=420, beds=1,baths=1, area=4200, url='https://www.google.com', image='https://image.com', 
    #                         coords={'latitude': 2000, 'longitude': 1000}, id=1, date=datetime.now(), cats=True, dogs=True, parking=False, 
    #                         laundry=True, apartment=True, townhouse=False, house=False)
    # print(jsonify(house))