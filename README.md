# Housing Search
## Cloning Repository
1. Clone the repository
2. Ensure that python3 is installed. Check via `python3 --version`
3. Open the python virtual environment from command line. \
Windows: `./env/Scripts/activate` \
Unix: `source env/Scripts/activate`
4. Run `python3 app.py`
5. Open `localhost`

## Using HousingSearch API
```
from utils import Filters, House
from housingsearch import search_all

filters = Filters(price=2000, baths=2, beds=4)
houses: list[House] = search_all(filters)
# sort by price
houses.sort(key=lambda house:house.price)
```
The list of housing results are temporarily cached for a day before a query is made again. This is to prevent 
making too many requests, so the IP address isn't banned from Craigslist or Zillow.

