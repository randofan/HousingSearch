from utils import House
from zillow import search_zillow
from craigslist import search_craigslist

def search_all(filters):
    houses = []
    zillow: list[House] = search_zillow(filters)
    craigslist: list[House] = search_craigslist(filters)
    houses.extend(zillow).extend(craigslist)
    return houses