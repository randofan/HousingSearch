from utils import House
from zillow import search_zillow
from craigslist import search_craigslist
from utils import Filters
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime, timedelta

def search_all(filters=Filters()):
    engine = create_engine('sqlite:///sqlalchemy.sqlite')
    Session = sessionmaker(bind=engine)
    with Session() as session:
        if session.query(House).first().time + timedelta(days=1) >= datetime.utcnow():
            print('Loading cached data...')
            return [house for house in session.query(House).all()]
        
        houses = []
        zillow: list[House] = search_zillow(filters)
        craigslist: list[House] = search_craigslist(filters)
        houses.extend(zillow)
        houses.extend(craigslist)
        
        session.query(House).delete()
        session.add_all(houses)
        session.commit()
    return houses

if __name__ == '__main__':
    l = search_all()
    print(l[0])
    print(len(l))