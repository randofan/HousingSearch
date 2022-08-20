import re
from conversions import zillow_convert, craigslist_convert
from enum import Enum

class TranslationType(Enum):
    ZILLOW = 0
    CRAIGSLIST = 1
    
class InvalidFilterException(Exception):
    pass

def getNum(num) -> float:
    res = re.sub("[^0-9|.]", "", num) if num else 0
    return float(res) if res != '' else 0


def TranslateZillow(user_query):
    k, v = user_query
    if isinstance(v, bool): 
        if isinstance(zillow_convert[k], tuple): return [(z, {'min': v}) for z in zillow_convert[k]]
        else: return [(zillow_convert[k], {'value': v})]
    elif isinstance(v, int) or isinstance(v, float): 
        if k == 'price': return [(zillow_convert[k], {'max': v})]
        else: return [(zillow_convert[k], {'min': v})]


def TranslateCraigslist(user_query):
    k, v = user_query
    if isinstance(v, bool):
        if k == 'cats' or k == 'dogs': return [(craigslist_convert[k], 1)]
        else: 
            t, nums = next(iter(craigslist_convert[k].items()))
            if isinstance(nums, int): return [(t, nums)]
            else: return [(t, n) for n in nums]
    else: return [(craigslist_convert[k], v)]


def Translate(filter, type):
    if not isinstance(filter, Filters): raise InvalidFilterException
    
    translation = [] # list of tuples containing key value pairs.
    pairs = vars(filter)
    for k,v in pairs.items():
        if v == False or v == 0: continue
        
        new_pair = []
        if type == TranslationType.ZILLOW: new_pair = TranslateZillow((k,v))
        elif type == TranslationType.CRAIGSLIST: new_pair = TranslateCraigslist((k,v))
        else: raise InvalidFilterException
        translation.extend(new_pair)
        
    return translation