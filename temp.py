def craigslist_filters(args):
    filters = dict()
    houses = []
    conversion = pycraigslist.housing.apa().get_filters()
    for filter, value in args.items():
        if filter in constants.housing_types:
            houses.append(filter)
        else:
            cg_filter = constants.craigslist[filter]
            cg_res = conversion[cg_filter]
            if cg_res == 'True/False':
                filters[cg_filter] = 'True'
            elif isinstance(cg_res, list):
                filters[cg_filter] = cg_res[:-1]
            else:
                filters[cg_filter] = value
    return filters


def craigslist():    
    houses = pycraigslist.housing.apa(site="seattle", zip_code="98105")
    filters = {'min_bedrooms': '10'}
    houses = list(pycraigslist.housing.apa(site="seattle", zip_code="98105", filters=filters).search())

    print(houses.get_filters())
    print(houses[0])