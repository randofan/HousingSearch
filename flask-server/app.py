from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from utils import House, Filters
from housingsearch import search_all


app = Flask(__name__)

### DO NOT RUN!!! OR ELSE CRAIGSLIST AND ZILLOW WILL BAN YOUR IP ###
@app.route('/', methods=['GET'])
def index():
    houses = []
    if request.args:
        # houses: list[House] = search_all(**filters)
        houses = [House('1234 Test Ln', 420, 1,1, 4200, 'https://www.google.com', 'https://image.com', {'latitude': 2000, 'longitude': 1000})]
    return houses


if __name__ == '__main__':
    app.run(debug=True)