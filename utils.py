from logging import Filter
import re
from constants import zillow_convert, craigslist_convert
from dataclasses import dataclass, field
import attr
from enum import Enum

class TranslationType(Enum):
    ZILLOW = 0
    CRAIGSLIST = 1

@dataclass(frozen=True)
class House:
    address: str = ''
    price: float = 0
    beds: float = 0
    baths: float = 0
    area: float = 0
    url: str = ''
    image: str = ''
    coords: dict[str, float] = field(default_factory=dict)
    
    def __hash__(self) -> int:
        return hash(str(self.coords)) # TODO check if I get duplicates still
    
    def __eq__(self, other):
        return self.coords == other.coords

@attr.s
class Filters:
    beds: int = attr.ib(validator=attr.validators.instance_of(int), default=0)
    baths: int = attr.ib(validator=attr.validators.instance_of(int), default=0)
    price: int = attr.ib(validator=attr.validators.instance_of(int), default=0)
    sqft: int = attr.ib(validator=attr.validators.instance_of(int), default=0)
    cats: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    dogs: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    parking: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    laundry: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    apartment: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    townhouse: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    house: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    
class InvalidFilterException(Exception):
    pass

def getNum(num) -> int:
    return int(re.sub("[^0-9|.]", "", num)) if num else 0


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


if __name__ == '__main__':
    pass