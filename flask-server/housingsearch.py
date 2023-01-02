from zillow import search_zillow
from craigslist import search_craigslist
from utils import CRAIGSLIST_RANGE
from models import Filters, House

def search_all(filters=Filters()) -> list[House]:
    houses: House = []
    houses.extend(search_craigslist(0, CRAIGSLIST_RANGE, filters))
    houses.extend(search_zillow(filters))
    houses.extend(search_craigslist(CRAIGSLIST_RANGE+1, CRAIGSLIST_RANGE, filters, ))
    return houses

if __name__ == '__main__':
    l = search_all()
    print(l[0])
    print(len(l))