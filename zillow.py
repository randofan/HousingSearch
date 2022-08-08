from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json
from constants import zillow_convert
from utils import getPrice, keys

def search_zillow(user_query={}):
    
    # Translate filters into URL arguments.
    translated_query = {}
    for k,v in user_query.items():
        try:
            if isinstance(v, bool): translated_query[zillow_convert[k]] = {'value': v}
            elif isinstance(v, int) or isinstance(v, float): translated_query[zillow_convert[k]] = {'min': v}
        except KeyError:
            print(f'"{k}" is not a valid key.\n')
            raise KeyError
    
    # Query constants.
    query = {"pagination": {}, 
             "isMapVisible":True, 
             "mapBounds":{"west":-122.34915592114258,"east":-122.21423007885743,"south":47.64551478474824,"north":47.67615329343806},
             "regionSelection":[{"regionId":99565,"regionType":7}],
             "isMapVisible":True,
             "filterState":{
                 "isForSaleForeclosure":{"value":False},
                 "isAllHomes":{"value":True},
                 "isAuction":{"value":False},
                 "isMultiFamily":{"value":False},
                 "isNewConstruction":{"value":False},
                 "isLotLand":{"value":False},
                 "isManufactured":{"value":False},
                 "isForSaleByOwner":{"value":False},
                 "isComingSoon":{"value":False},
                 "isForSaleByAgent":{"value":False},
                 "isForRent":{"value":True}
             }
    }
    query['filterState'].update(translated_query)
    wants = {"cat1":['mapResults']}
    
    ds = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=ds)

    # Must visit zillow homepage first to set cookies.
    driver.get("https://www.zillow.com/")
    driver.get(f"https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={json.dumps(query)}&wants={json.dumps(wants)}")
    
    try:
        raw_data = driver.find_element(By.TAG_NAME, "pre").text
    except Exception:
        print(f'query incorrectly created or captcha lol fuck zillow.\n')
        driver.quit()
        raise AttributeError
        
    driver.quit()
    
    response = json.loads(raw_data)["cat1"]["searchResults"]["mapResults"]
    houses = []
    for r in response:
        house = dict()
        try:
            house.update({'address': r['address'], 
                    'price': getPrice(r['price']), 
                    'beds': r['beds'] if 'beds' in r else r['minBeds'], 
                    'baths': r['baths'] if 'baths' in r else r['minBaths'], 
                    'area': r['area'] if 'area' in r else r['minArea'], 
                    'url': f'https://www.zillow.com{r["detailUrl"]}', 
                    'image': r['imgSrc'],
                    'coords': r['latLong']})
            
            if house['address'] == '--':
                house['address'] = r['detailUrl'].split('/')[2].replace('-', ' ')
            
            if set(house) != keys:
                print(f'House does not contain all required keys.')
                raise KeyError
            houses.append(house)
            
        except Exception:
            print(f'There was an error with one of the listings:\n\n{house}\n\n{r}')
        
    del response, raw_data
    return houses
    
    
def test():
    ds = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=ds)

    # Must visit zillow homepage first to set cookies.
    driver.get("https://www.zillow.com/")
    

if __name__ == '__main__':

    houses = search_zillow()
    print(len(houses))
    # test()