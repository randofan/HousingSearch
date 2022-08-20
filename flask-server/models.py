from dataclasses import dataclass
import attr
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

@dataclass
class House(db.Model):
    __tablename__ = 'house'
    address: str
    price: float
    beds: float
    baths: float
    area: float
    url: str
    image: str
    coords: dict[str, int]
    id: int
    date: datetime
    cats: bool
    dogs: bool
    parking: bool
    laundry: bool
    apartment: bool
    townhouse: bool
    house: bool
    
    address = db.Column(db.String(80), default = '')
    price = db.Column(db.Float, default = 0.0)
    beds = db.Column(db.Float, default = 0.0)
    baths = db.Column(db.Float, default = 0.0)
    area = db.Column(db.Float, default = 0.0)
    url = db.Column(db.String(200), default = '')
    image = db.Column(db.String(200), default = '')
    coords = db.Column(db.PickleType, nullable=False)
    id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    cats: bool = db.Column(db.Boolean, default=False)
    dogs: bool = db.Column(db.Boolean, default=False)
    parking: bool = db.Column(db.Boolean, default=False)
    laundry: bool = db.Column(db.Boolean, default=False)
    apartment: bool = db.Column(db.Boolean, default=False)
    townhouse: bool = db.Column(db.Boolean, default=False)
    house: bool = db.Column(db.Boolean, default=False)
    
    def __repr__(self) -> str:
        return f'''(address: {self.address}, price: {self.price}, beds: {self.beds}, baths: {self.baths}, area: {self.area}, url: {self.url}, image: {self.image}, coords: {self.coords}, time: {self.time})'''

@attr.s
class Filters:
    beds: int = attr.ib(validator=attr.validators.instance_of(int), default=0)
    baths: int = attr.ib(validator=attr.validators.instance_of(int), default=0)
    price: int = attr.ib(validator=attr.validators.instance_of(int), default=0)
    area: int = attr.ib(validator=attr.validators.instance_of(int), default=0)
    cats: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    dogs: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    parking: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    laundry: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    apartment: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    townhouse: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    house: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)