from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json
import requests
from utils import getNum, House, Filters, Translate, TranslationType

def use_selenium(query, wants):
    ds = Service('chromedriver.exe')
    with webdriver.Chrome(service=ds) as driver:
        # Must visit zillow homepage first to set cookies.
        driver.get("https://www.zillow.com/seattle-wa-98105/rentals/")
        driver.get(f"https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={json.dumps(query)}&wants={json.dumps(wants)}")
        
        res = driver.find_element(By.TAG_NAME, "pre")
        if res: return res.text
        else:
            print('The dreaded Zillow Captcha with selenium...Unfortunately try again later')
            return None
        
def use_requests(query, wants):
    req_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    with requests.Session() as s:
        url = f"https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={json.dumps(query)}&wants={json.dumps(wants)}"
        r = s.get(url, headers=req_headers)
    if r: return r.text
    else:
        print('The dreaded Zillow Captcha with requests...Unfortunately try again later')
        return None

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
                 "isForRent":{"value":True},
                 "sortSelection":{"value":"paymenta"}
             }
    }
    query['filterState'].update(dict(Translate(user_query, TranslationType.ZILLOW)))
    wants = {"cat1":['mapResults']}
    
    raw_data = use_requests(query, wants)
    if not raw_data: raw_data = use_selenium(query, wants)
    
    houses = list()
    if not raw_data: 
        print('Neither using Selenium nor Requests worked. No Response.')
        return houses
    
    response = json.loads(raw_data)["cat1"]["searchResults"]["mapResults"]
    for r in response:
        try:          
            house = House(address=r['detailUrl'].split('/')[2].replace('-', ' ') if r['address'] == '--' else r['address'],
                          price=getNum(r['price']), beds=r['beds'] if 'beds' in r else 0, 
                          baths=r['baths'] if 'baths' in r else 0, area=r['area'] if 'area' in r else 0,
                          url=f'https://www.zillow.com{r["detailUrl"]}', image=r['imgSrc'], coords=r['latLong'])
            house.id = id(house)
            houses.append(house)    
        except KeyError as e: print(f'ZILLOW: There was an error parsing https://www.zillow.com{r["detailUrl"]} with {e}')
        
    return houses
    

if __name__ == '__main__':
    houses = search_zillow(Filters(beds=3, price=2200))
    print(houses.pop())
    print(len(houses))
    