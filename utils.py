import re
from constants import zillow_convert, craigslist_convert

def getNum(num):
    return re.sub("[^0-9|.]", "", num) if num else None


def TranslateZillow(user_query):
    translated_query = {}
    for k,v in user_query.items():
        try:
            if isinstance(v, bool): translated_query[zillow_convert[k]] = {'value': v}
            elif isinstance(v, int) or isinstance(v, float): 
                for z in zillow_convert[k]:
                    translated_query[z] = {'min': v}
        except KeyError:
            print(f'"{k}" is not a valid key.\n')
            raise KeyError
    return translated_query


def TranslateCraigslist(user_query):
    translated_query = {}
    for k,v in user_query.items():
        try:
            if isinstance(v, float) or isinstance(v, int): translated_query[craigslist_convert[k]] = v
            else:
                if k == 'cats' or k == 'dogs': translated_query[craigslist_convert[k]] = 1
                else: translated_query.update({t: n for t,n in craigslist_convert[k]})
        except KeyError:
            print(f'"{k}" is not a valid key.\n')
            raise KeyError
    return translated_query

class House:
    def __init__(self):
        self.address = ''
        self.price = 0
        self.beds = 0
        self.baths = 0
        self.area = 0
        self.url = ''
        self.image = ''
        self.coords = ''
        self.platform = ''
        
class Filters:
    def __init__(self):
        self.beds = 0
        self.baths = 0
        self.price = 0
        self.sqft = 0
        self.cats = False
        self.dogs = False
        self.parking = False
        self.laundry = False
        self.apartment = False
        self.townhouse = False
        self.house = False