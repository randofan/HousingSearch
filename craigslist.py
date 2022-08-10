import asyncio
import requests
from bs4 import BeautifulSoup
from utils import TranslateCraigslist, getNum, House, Filters
import time
from httpx import AsyncClient


async def getURL(url):
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    if not soup.find(class_='result-row'): return []
    
    # limit to only 1 requests so I don't get banned
    urls = (url['href'] for url in soup.find_all('a', class_='result-title hdrlnk')[:1])

    async with AsyncClient() as client:
        tasks = (client.get(url) for url in urls)
        reqs = await asyncio.gather(*tasks)
        
    soups = [BeautifulSoup(req.text, 'html.parser') for req in reqs]
    return zip(soups, urls)


def search_craigslist(user_query={}):
    
    query = {'bundleDuplicates':1, 
             'postal':98105, 
             'availabilityMode':0, 
             'sale_date':'all+dates'}
    query.update(TranslateCraigslist(user_query))
    
    query = "&".join(f'{k}={v}' for k,v in query.items())
    houses = []
    
    i = 0
    while True:
        soups_url = asyncio.run(getURL(f'https://www.craigslist.org/search/apa?s={i}&{query}'))
        if not soups_url: break
        
        for soup, url in soups_url:
            house = House()
            house.address = soup.find('div', class_='mapaddress')
            house.price = getNum(soup.find('span', class_='price').text)
            house.url = url
            house.image = soup.find('img')
            
            map_obj = soup.find(id='map')
            house.coords = {'latitude': map_obj['data-latitude'], 'longitude': map_obj['data-longitude']}
            
            attr = soup.find_all(class_='shared-line-bubble')
            for a in attr:
                a = str(a)
                elem = a.split('<b>')
                for e in elem:
                    if 'BR' in e: house.beds = getNum(e) 
                    elif 'Ba' in e: house.baths = getNum(e) 
                    elif 'ft' in e: house.area = getNum(e)[:-1] 
            
            houses.append(house)
        i += 120
        
    return houses

if __name__ == '__main__':
    l = search_craigslist()
    print(l)