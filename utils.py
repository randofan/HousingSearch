import re

def getPrice(price):
    return re.sub("[^0-9|.]", "", price)

keys = {'address', 'price', 'beds', 'baths', 'area', 'url', 'image', 'coords'}