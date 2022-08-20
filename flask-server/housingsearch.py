from zillow import search_zillow
from craigslist import search_craigslist
from constants import DATE_LAST_CHECKED, REFRESH_RATE
from models import Filters

def search_all(filters=Filters()):
    houses = []
    houses.extend(search_zillow(filters))
    houses.extend(search_craigslist(DATE_LAST_CHECKED + REFRESH_RATE, filters))
    return houses

if __name__ == '__main__':
    l = search_all()
    print(l[0])
    print(len(l))