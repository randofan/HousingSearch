from dataclasses import dataclass, field
import attr

@dataclass(frozen=True)
class House:
    address: str
    price: float
    beds: float
    baths: float
    area: float
    url: str
    image: str
    pets: bool
    parking: bool
    laundry: bool
    coords: dict[str, int] = field(default_factory=dict)

@attr.s
class Filters:
    beds: int = attr.ib(validator=attr.validators.instance_of(int), default=0)
    baths: int = attr.ib(validator=attr.validators.instance_of(int), default=0)
    price: int = attr.ib(validator=attr.validators.instance_of(int), default=0)
    area: int = attr.ib(validator=attr.validators.instance_of(int), default=0)
    pets: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    parking: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    laundry: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    apartment: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    townhouse: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)
    house: bool = attr.ib(validator=attr.validators.instance_of(bool), default=False)