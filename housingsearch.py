from utils import House
from zillow import search_zillow
from craigslist import search_craigslist
from utils import Filters

def search_all(filters=Filters()):
    houses = []
    zillow: list[House] = search_zillow(filters)
    craigslist: list[House] = search_craigslist(filters)
    houses.extend(zillow)
    houses.extend(craigslist)
    return houses

if __name__ == '__main__':
    l = search_all()
    print(l[0])
    print(len(l))