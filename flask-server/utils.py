import re
from conversions import zillow_convert, craigslist_convert
from enum import Enum
from utils import Filters

CRAIGSLIST_RANGE = 20

class TranslationType(Enum):
    ZILLOW = 0
    CRAIGSLIST = 1
    APARTMENTS = 2
    
class InvalidFilterException(Exception):
    pass


# Helper function to get float from string.
def getNum(num) -> float:
    res = re.sub("[^0-9|.]", "", num) if num else 0
    return float(res) if res != '' else 0


# Translate a specific Filters query into its Zillow equivalent.

# parameters:
# - user_query: key-value pair within Filters.

# returns: list with one tuple containing translation.
def TranslateZillow(user_query):
    k, v = user_query
    if isinstance(v, bool): 
        if isinstance(zillow_convert[k], tuple): return [(z, {'min': v}) for z in zillow_convert[k]]
        else: return [(zillow_convert[k], {'value': v})]
    elif isinstance(v, int) or isinstance(v, float): 
        if k == 'price': return [(zillow_convert[k], {'max': v})]
        else: return [(zillow_convert[k], {'min': v})]


# Translate a specific Filters query into its Craigslist equivalent.

# parameters:
# - user_query: key-value pair within Filters.

# returns: list with one tuple containing translation.
def TranslateCraigslist(user_query):
    k, v = user_query
    if isinstance(v, bool):
        if k == 'pets': return [(t, 1) for t in craigslist_convert[k]]
        else: 
            t, nums = list(craigslist_convert[k].items())[0]
            if isinstance(nums, int): return [(t, nums)]
            else: return [(t, n) for n in nums]
    else: return [(craigslist_convert[k], v)]


# Translate Filters object.

# parameters:
# - filter: Filters object with specified search constraints.
# - type: which website to translate to.

# throws InvalidFilterException if filter is not a Filters objects or type is not a valid type.
# returns: list of tuples with website-specific query parameters translation.
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