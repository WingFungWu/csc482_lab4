from yelpapi import YelpAPI

api_key = 'QdWuuYK67ZrY2Sv8Ow5xS5a1qFeL4WBds4uo6kp9tC1bBJw7CNoUPQLTd001Z2xOsRrjVFD0gg1ooVsFazDQmxRkbwso1wwZpCjL9OOm9uDwC2-tqwXytmVySQgIZHYx'

yelp_api = YelpAPI(api_key)

def getNumReviews(resturant, location):
    response = yelp_api.search_query(term=resturant, location=location, limit=1)
    num_reviews = response['businesses'][0]['review_count']
    ret_str = "{a} in {b} has {c} reviews".format(a=resturant, b=location, c=num_reviews)
    return ret_str

def getCategory(resturant, location):
    response = yelp_api.search_query(term=resturant, location=location, limit=1)
    category = response['businesses'][0]['categories'][0]['alias']
    ret_str = "{a} in {b} is {c}".format(a=resturant, b=location, c=category)
    return ret_str

def getRating(resturant, location):
    response = yelp_api.search_query(term=resturant, location=location, limit=1)
    rating = response['businesses'][0]['rating']
    ret_str = "{a} in {b} has a rating of {c}".format(a=resturant, b=location, c=str(rating))
    return ret_str

def getPrice(resturant, location):
    response = yelp_api.search_query(term=resturant, location=location, limit=1)
    price = len(response['businesses'][0]['price'])
    ret_str = "{a} in {b} has {c} dollar signs".format(a=resturant, b=location, c=str(price))
    return ret_str

def getLocation(resturant, location):
    response = yelp_api.search_query(term=resturant, location=location, limit=1)
    address = response['businesses'][0]['location']['address1'] + " " + response['businesses'][0]['location']['city'] + " " + response['businesses'][0]['location']['zip_code']
    ret_str = "The address for {a} is {b}".format(a=resturant, b=address)
    return ret_str

def getPhonNum(resturant, location):
    response = yelp_api.search_query(term=resturant, location=location, limit=1)
    phone_num = response['businesses'][0]['display_phone']
    ret_str = "The phone number for {a} in {b} is {c}".format(a=resturant, b=location, c=phone_num)
    return ret_str

