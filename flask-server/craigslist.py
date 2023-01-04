import asyncio
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from utils import Translate, getNum, TranslationType
from models import House, Filters
from httpx import AsyncClient

async def getURL(urls):
    async with AsyncClient() as client:
        tasks = (client.get(url) for url in urls)
        reqs = await asyncio.gather(*tasks)
        
    soups = [BeautifulSoup(req.text, 'html.parser') for req in reqs]
    return soups

def search_craigslist(start: int, range: int, user_query: Filters=Filters()):
    
    query = [('bundleDuplicates',1), 
             ('postal',98105), 
             ('availabilityMode',0), 
             ('sale_date','all+dates'),
             ('sort', 'priceasc')]
    query.extend(Translate(user_query, TranslationType.CRAIGSLIST))
    query = "&".join(f'{k}={v}' for k,v in query)
    
    session = HTMLSession()
    soup = session.get(f'https://www.craigslist.org/search/apa?s=0&{query}')
    soup.html.render(sleep=1)
    
    # return empty array if no results found
    if not soup.find('a.cl-results-page'): 
        print("no results found")
        return []
    
    urls = [url.attrs['href'] for url in soup.find('a.titlestring')]
    limit_url = urls[min(start,len(urls)):min(start+range,len(urls))]
    soups = asyncio.run(getURL(limit_url))
    
    houses = []
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
            
            house = House(address=address, price=price, beds=beds, baths=baths, area=area, url=url, 
                            image=image, coords=coords, pets=user_query.pets, 
                            parking=user_query.parking, laundry=user_query.laundry)
            houses.append(house)
        except Exception as e: print(f'CRAIGSLIST: There was an error parsing {url} with {e}')

    return houses

if __name__ == '__main__':
    print(search_craigslist(0, 2))