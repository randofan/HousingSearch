import asyncio
import random
import requests
from bs4 import BeautifulSoup
from utils import Translate, getNum, TranslationType
from models import House, Filters
import time 
from httpx import AsyncClient
from datetime import datetime

async def getURL(urls):
    async with AsyncClient() as client:
        tasks = (client.get(url) for url in urls)
        reqs = await asyncio.gather(*tasks)
        
    soups = [BeautifulSoup(req.text, 'html.parser') for req in reqs]
    return soups

def search_craigslist(DATE_REFRESH, user_query=Filters()):
    
    query = [('bundleDuplicates',1), 
             ('postal',98105), 
             ('availabilityMode',0), 
             ('sale_date','all+dates'),
             ('sort', 'priceasc')]
    query.extend(Translate(user_query, TranslationType.CRAIGSLIST))
    query = "&".join(f'{k}={v}' for k,v in query)
    
    soup = BeautifulSoup(requests.get(f'https://www.craigslist.org/search/apa?s=0&{query}').content, 'html.parser')
    # return empty array if no results found
    if not soup.find(class_='result-row'): return []
    
    # TODO log how long this array is overtime
    urls = [url.find('a', class_='result-title hdrlnk')['href'] for url in soup.find_all('div', class_='result-info') 
            if (url.find('time', class_='result-date')['datetime'] < DATE_REFRESH and 
                not House.query.get_or_404(getNum(url.find('a', class_='result-title hdrlnk')['data-id'])))]
    
    houses = list()
    
    prev = 0
    while True:
        # limit to only 6-22 requests so I don't get banned
        REQUESTS = random.randrange(6,22)
        if prev+REQUESTS > len(urls)-1: break
        
        limit_url = urls[prev:(prev+REQUESTS)]
        soups = asyncio.run(getURL(limit_url))
        for soup, url in zip(soups, limit_url):
            
            beds, baths, area = 0,0,0
            attr = soup.find_all(class_='shared-line-bubble')
            for a in attr:
                a = str(a)
                elem = a.split('<b>')
                for e in elem:
                    if 'BR' in e: beds += getNum(e) 
                    elif 'Ba' in e: baths += getNum(e) 
                    elif 'ft' in e: area += (getNum(e) // 10)
            
            try:
                address = soup.find('div', class_='mapaddress').text
                price = getNum(soup.find('span', class_='price').text)
                image = soup.find('img')['src']
                
                map_obj = soup.find(id='map')
                coords = {'latitude': float(map_obj['data-latitude']), 'longitude': float(map_obj['data-longitude'])}
                id = hash(f"{getNum(soup.find('div', class_='postinginfos').find('p', class_='postinginfo').text)}c")
                date = datetime(soup.find('time', class_='date timeago')['datetime'])
                
                house = House(address=address, price=price, beds=beds, baths=baths, area=area, url=url, 
                              image=image, coords=coords, id=id, date=date, cats=user_query.cats, dogs=user_query.dogs, 
                              parking=user_query.parking, laundry=user_query.laundry, apartment=user_query.apartment,
                              townhouse=user_query.townhouse, house=user_query.house)
                houses.append(house)
            except Exception as e: print(f'CRAIGSLIST: There was an error parsing {url} at {prev} with {e}')
        prev += REQUESTS
        time.sleep(random.random() * 2)
    return houses

if __name__ == '__main__':
    pass