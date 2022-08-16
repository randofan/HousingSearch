from sqlalchemy.orm import sessionmaker
from utils import base, House
from sqlalchemy import create_engine

engine = create_engine('sqlite:///sqlalchemy.sqlite')
session = sessionmaker(bind=engine)()

session.query(House).delete()
# for s in session.query(House).all():
#     print(s)
    
house = House(address='123 Test Ave', price=9999, beds=0, baths=0, coords={'latitude':-2222.22, 'longitude':1000.23},
              url='https://www.google.com', area=234, image='https://www.googleimage.com')
house.id = id(house)
session.add(house)
session.commit()
for s in session.query(House).all():
    print(s)

# base.metadata.create_all(engine)