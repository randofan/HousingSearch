from selenium import webdriver, common
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json
import time
from utils import getNum, House, Filters, Translate, TranslationType

def search_zillow(user_query=Filters()):
   
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
    query['filterState'].update(dict(Translate(user_query, TranslationType.ZILLOW)))
    wants = {"cat1":['mapResults']}
    
    ds = Service('chromedriver.exe')
    with webdriver.Chrome(service=ds) as driver:
        # Must visit zillow homepage first to set cookies.
        driver.get("https://www.zillow.com/")
        driver.get(f"https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={json.dumps(query)}&wants={json.dumps(wants)}")
        time.sleep(20)
        raw_data = None
        try: raw_data = driver.find_element(By.TAG_NAME, "pre").text
        except common.exceptions.NoSuchElementException: print(f'The dreaded Zillow Captcha...Unfortunately try again later')
    
    houses = set()
    if not raw_data: return houses
    
    response = json.loads(raw_data)["cat1"]["searchResults"]["mapResults"]
    for r in response:
        try:          
            house = House(r['detailUrl'].split('/')[2].replace('-', ' ') if r['address'] == '--' else r['address'],
                          getNum(r['price']), r['beds'] if 'beds' in r else 0, 
                          r['baths'] if 'baths' in r else 0, r['area'] if 'area' in r else 0,
                          f'https://www.zillow.com{r["detailUrl"]}', r['imgSrc'], r['latLong'])
            houses.add(house)    
        except KeyError: print(f'ZILLOW: There was an error parsing https://www.zillow.com{r["detailUrl"]}')
        
    return houses
    

if __name__ == '__main__':
    # ds = Service('chromedriver.exe')
    # driver = webdriver.Chrome(service=ds)
    # driver.get("https://www.zillow.com/")
    # driver.get('https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"pagination":{},"usersSearchTerm":"98105","mapBounds":{"west":-122.31194831768799,"east":-122.25143768231202,"south":47.62593719553573,"north":47.69571206415039},"regionSelection":[{"regionId":99565,"regionType":7}],"isMapVisible":true,"filterState":{"isForSaleByAgent":{"value":false},"isForSaleByOwner":{"value":false},"isNewConstruction":{"value":false},"isForSaleForeclosure":{"value":false},"isComingSoon":{"value":false},"isAuction":{"value":false},"isForRent":{"value":true},"isAllHomes":{"value":true},"isMultiFamily":{"value":false},"isManufactured":{"value":false},"isLotLand":{"value":false}},"isListVisible":true,"mapZoom":14}&wants={"cat1":["listResults","mapResults"]}')
    
    houses = search_zillow(Filters(beds=3, price=1000))
    print(len(houses))