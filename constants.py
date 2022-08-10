'''
https://seattle.craigslist.org/search/apa?bundleDuplicates=1&postal=98105&
min_price=500&max_price=3000&min_bedrooms=3&min_bathrooms=2&minSqft=100&availabilityMode=0&
pets_cat=1&pets_dog=1&housing_type=1&housing_type=6&housing_type=9&laundry=1&laundry=4&laundry=2&
laundry=3&parking=1&parking=2&parking=3&parking=4&parking=5&parking=6&sale_date=all+dates
'''

craigslist_convert = {
    'beds': 'min_bedrooms', # int
    'price': 'min_price', # int
    'baths': 'min_bathrooms', # int
    'sqft': 'minSqft', # int
    'cats': 'pets_cat', # 1=True
    'dogs': 'pets_dog', # 1=True
    'parking': {'parking': (1,2,3,4,5,6)},
    'laundry': {'laundry': (1,2,3,4)},
    'apartment': {'housing_type': 1},
    'townhouse': {'housing_type': 6},
    'house': {'housing_type': 9}
}


zillow_convert = {
    'beds': 'beds', # int
    'price': 'monthlyPayment', # int
    'baths': 'baths',  # int
    'sqft': 'sqft', # int
    'cats': 'onlyRentalCatsAllowed', # bool
    'dogs': ('onlyRentalLargeDogsAllowed', 'onlyRentalSmallDogsAllowed'), # bool
    'parking': 'onlyRentalParkingAvailable', # bool
    'laundry': 'onlyRentalInUnitLaundry', # bool
    'apartment': 'isApartment', # bool
    'townhouse': 'isTownhouse', # bool
    'house': 'isSingleFamily' # bool
}
