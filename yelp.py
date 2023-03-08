from yelpapi import YelpAPI
import nltk
import random
from difflib import get_close_matches

api_key = 'QdWuuYK67ZrY2Sv8Ow5xS5a1qFeL4WBds4uo6kp9tC1bBJw7CNoUPQLTd001Z2xOsRrjVFD0gg1ooVsFazDQmxRkbwso1wwZpCjL9OOm9uDwC2-tqwXytmVySQgIZHYx'
yelp_api = YelpAPI(api_key)

def error_msg(resturant, location):
    ret_str = "I could not find the resturant {a} in {b}".format(a=resturant, b=location)
    return ret_str
    
def checkEditDistance(request, response):
    distance = nltk.edit_distance(request, response['businesses'][0]['name'].lower())
    return distance < 5

def getNumReviews(resturant, location):
    response = yelp_api.search_query(term=resturant, location=location, limit=1)
    if response['businesses'] and checkEditDistance(resturant, response):
        num_reviews = response['businesses'][0]['review_count']
        ret_str = "{a} in {b} has {c} reviews".format(a=resturant, b=location, c=num_reviews)
        return ret_str
    else:
        return error_msg(resturant, location)

def getReview(resturant, location):
    response = yelp_api.search_query(term=resturant, location=location, limit=1)
    if response['businesses'] and checkEditDistance(resturant, response):
        id = response['businesses'][0]['id']
        review = random.choice(yelp_api.reviews_query(id=id, locale="en_US")["reviews"])
        ret_str = "Here is a random review of {a} in {b}. {c} gave the resturant a rating of {d} stars and said: {e}".format(a=resturant, b=location, c=review['user']['name'], d=review['rating'], e=review['text'])
        return ret_str
    else:
        return error_msg(resturant, location)

def getCategory(resturant, location):
    response = yelp_api.search_query(term=resturant, location=location, limit=1)
    if response['businesses'] and checkEditDistance(resturant, response):
        category = response['businesses'][0]['categories'][0]['title']
        ret_str = "{a} in {b} is {c}".format(a=resturant, b=location, c=category)
        return ret_str
    else:
        return error_msg(resturant, location)

def getRating(resturant, location):
    response = yelp_api.search_query(term=resturant, location=location, limit=1)
    if response['businesses'] and checkEditDistance(resturant, response):
        rating = response['businesses'][0]['rating']
        ret_str = "{a} in {b} has a rating of {c}".format(a=resturant, b=location, c=str(rating))
        return ret_str
    else:
        return error_msg(resturant, location)

def getPrice(resturant, location):
    response = yelp_api.search_query(term=resturant, location=location, limit=1)
    if response['businesses'] and checkEditDistance(resturant, response):
        price = len(response['businesses'][0]['price'])
        ret_str = "{a} in {b} has {c} dollar signs".format(a=resturant, b=location, c=str(price))
        return ret_str
    else:
        return error_msg(resturant, location)

def getLocation(resturant, location):
    response = yelp_api.search_query(term=resturant, location=location, limit=1)
    if response['businesses'] and checkEditDistance(resturant, response):
        address = response['businesses'][0]['location']['address1'] + " " + response['businesses'][0]['location']['city'] + " " + response['businesses'][0]['location']['zip_code']
        ret_str = "The address for {a} is {b}".format(a=resturant, b=address)
        return ret_str
    else:
        return error_msg(resturant, location)

def getPhonNum(resturant, location):
    response = yelp_api.search_query(term=resturant, location=location, limit=1)
    if response['businesses'] and checkEditDistance(resturant, response):
        phone_num = response['businesses'][0]['display_phone']
        ret_str = "The phone number for {a} in {b} is {c}".format(a=resturant, b=location, c=phone_num)
        return ret_str
    else:
        return error_msg(resturant, location)

