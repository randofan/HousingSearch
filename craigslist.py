import asyncio
import requests
from bs4 import BeautifulSoup
from utils import Translate, getNum, House, Filters, TranslationType
import time
from httpx import AsyncClient


async def getURL(url):
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    if not soup.find(class_='result-row'): return []
    
    # limit to only 1 requests so I don't get banned
    urls = list(url['href'] for url in soup.find_all('a', class_='result-title hdrlnk')[:1])

    async with AsyncClient() as client:
        tasks = (client.get(url) for url in urls)
        reqs = await asyncio.gather(*tasks)
        
    soups = [BeautifulSoup(req.text, 'html.parser') for req in reqs]
    return zip(soups, urls)


def search_craigslist(user_query=Filters()):
    
    query = [('bundleDuplicates',1), 
             ('postal',98105), 
             ('availabilityMode',0), 
             ('sale_date','all+dates')]
    query.extend(Translate(user_query, TranslationType.CRAIGSLIST))
    
    query = "&".join(f'{k}={v}' for k,v in query)
    
    i = 0
    # while True:
    soups_url = asyncio.run(getURL(f'https://www.craigslist.org/search/apa?s={i}&{query}'))
    # if not soups_url: break
    
    houses = set()
    for soup, url in soups_url:
        
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

            houses.add(House(address, price, beds, baths, area, url, image, coords))
        except AttributeError: print(f'CRAIGSLIST: There was an error parsing {url}')
        
    i += 120
        
    return houses

if __name__ == '__main__':
    s = search_craigslist()
    print(s)