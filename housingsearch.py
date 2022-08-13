from utils import House
from zillow import search_zillow
from craigslist import search_craigslist

def search_all(filters):
    houses = []
    zillow: set[House] = search_zillow(filters)
    craigslist: set[House] = search_craigslist(filters)
    for house in zillow: 
        if house in craigslist: craigslist.remove(house)
    houses.extend(zillow).extend(craigslist)
    return houses