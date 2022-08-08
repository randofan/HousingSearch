import asyncio
import requests
from bs4 import BeautifulSoup
from utils import getNum
import time
from httpx import AsyncClient


async def getURL(url):
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    urls = (url['href'] for url in soup.find_all('a', class_='result-title hdrlnk'))
    
    async with AsyncClient() as client:
        tasks = (client.get(url) for url in urls)
        reqs = await asyncio.gather(*tasks)
        
    soups = [BeautifulSoup(req.text, 'html.parser') for req in reqs]
    print(len(soups))


if __name__ == '__main__':
    asyncio.run(getURL('https://seattle.craigslist.org/search/apa'))      


def search_craigslist(user_query={}):
    
    query = {'bundleDuplicates':1, 
             'postal':98105, 
             'availabilityMode':0, 
             'sale_date':'all+dates'}
    
    # TODO append translated user queries
    
    query = "&".join(f'{k}={v}' for k,v in query.items())
    i = 0
    # while True:
    page = requests.get(f'https://www.craigslist.org/search/apa?s={i}&{query}')
    soup = BeautifulSoup(page.content, 'html.parser')
    urls = soup.find_all('a', class_='result-title hdrlnk')['href']
    
    
    # if not raw_data: break
    
    async def parse_listing(data):
        # try:
            url = data.find('a', class_='result-title hdrlnk')['href']
            
            house = {'price': getPrice(str(data.find('span', class_='price'))), 
                    'url': url}
            
            house_soup = await BeautifulSoup(client.get(url).text, 'html.parser')
            
            map_obj = house_soup.find(id='map')
            house['coords'] = {'latitude': map_obj['data-latitude'], 'longitude': map_obj['data-longitude']}
            
            image = house_soup.find('img')
            house['image'] = image['src'] if image else None
            
            address = house_soup.find('div', class_='mapaddress')
            house['address'] = address.text if address else None
            
            attr = house_soup.find_all(class_='shared-line-bubble')
            for a in attr:
                a = str(a)
                elem = a.split('<b>')
                for e in elem:
                    if 'BR' in e: house['beds'] = getPrice(e) 
                    elif 'Ba' in e: house['baths'] = getPrice(e) 
                    elif 'ft' in e: house['area'] = getPrice(e)[:-1] 
            
            if 'beds' not in house: house['beds'] = 0
            if 'baths' not in house: house['baths'] = 0
            if 'area' not in house: house['area'] = 0
            
            houses.append(house)
            
        # except Exception:
        #     print(f'There was an error with one of the listings: \n\n')
            
    for data in raw_data:
        asyncio.run(parse_listing(data))
    
            
    i += 120
        
    return houses

def test():
    start = time.time()
    page = requests.get(f'https://www.craigslist.org/search/apa?s=0')
    print(time.time() - start)
    start = time.time()
    soup = BeautifulSoup(page.content, 'html.parser')
    print(time.time() - start)
    
