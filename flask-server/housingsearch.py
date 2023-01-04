from zillow import search_zillow
from craigslist import search_craigslist
from models import Filters, House
import time
import json
import dataclasses

CRAIGSLIST_RANGE = 20

def search_all(filters=Filters()) -> list[House]:
    houses: House = []
    # houses.extend(search_craigslist(0, CRAIGSLIST_RANGE, filters))
    houses.extend(search_zillow(filters))
    time.sleep(2)
    return houses

if __name__ == '__main__':
    print(json.dumps([dataclasses.asdict(house) for house in search_all()]))