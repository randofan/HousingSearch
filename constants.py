craigslist = {
    'beds': 'min_bedrooms',
    'price': 'min_price',
    'baths': 'min_bathrooms', 
    'sqft': 'min_ft2',
    'cats': 'cats_ok',
    'dogs': 'dogs_ok',
    'parking': 'parking', # needs a list argument
    'laundry': 'laundry', # needs a list argument
    'apartment': True,
    'townhouse': True,
    'house': True
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