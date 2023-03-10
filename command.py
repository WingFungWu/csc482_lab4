import nltk, weather, list , numeric, re, yelp

def get_city(pos):
    city_name = []
    for word, gram in pos:
        if gram == "NNP":
            city_name.append(word)
    return " ".join(city_name)

def run_command(text):
    tokens = nltk.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    if "weather" in tokens:
        city = get_city(pos)
        if len(city) == 0:
            return "Please specify a city"
        else:
            if "celsius" in tokens or "Celsius" in tokens:
                return weather.get_current_weather(city, f=False, c=True)
            elif "kelvin" in tokens or "kelvin" in tokens:
                return weather.get_current_weather(city, f=False, c=False)
            return weather.get_current_weather(city)
    elif ("highs" in tokens and "lows" in tokens) or ("high" in tokens and "low" in tokens):
        city = get_city(pos)
        if len(city) == 0:
            return "Please specify a city"
        else:
            if "celsius" in tokens or "Celsius" in tokens:
                return weather.get_high_low(city, f=False, c=True)
            elif "kelvin" in tokens or "kelvin" in tokens:
                return weather.get_high_low(city, f=False, c=False)
            return weather.get_high_low(city)
    elif "wind" in tokens or "winds" in tokens:
        city = get_city(pos)
        if len(city) == 0:
            return "Please specify a city"
        else:
            return weather.get_wind(city)
    elif "list" in tokens:
        if "create" in tokens:  #create new ... list  // create a new ... list // creat a new ... list please
            return list.createList( tokens[tokens.index("list")-1] )
        elif "add" in tokens:   #add ... to ... list // add ... to my ... list
            items = ' '.join(tokens[tokens.index("add")+1:len(tokens)-tokens[-1:0:-1].index("to") -  1])
            return list.addToList(tokens[tokens.index("list")-1], items)
        elif "remove" in tokens:  #remove ... from ... list  // remove ... from my ... list
            items = ' '.join(tokens[tokens.index("remove")+1:len(tokens)-tokens[-1:0:-1].index("from") -  1])
            return list.removeFromList(tokens[tokens.index("list")-1], items )
        elif "delete" in tokens:  #delete ... list // delete my ... list
            return list.deleteList(tokens[tokens.index("list")-1])
        elif "read" in tokens:  #read ... list  // read from my ...list
            return list.readList( tokens[tokens.index("list")-1] )
        elif "clear" in tokens: #clear ... list // clear all items in my ... list
            return list.clearList( tokens[tokens.index("list")-1] )
        else:
            return "I cannot understand your command"
    elif "many" in tokens and "yelp" in tokens and "reviews" in tokens:
        # get number of yelp reviews
        resturant = " ".join(tokens[tokens.index("does")+1: tokens.index("in")])
        city = " ".join(tokens[tokens.index("in")+1: tokens.index("have")])
        return yelp.getNumReviews(resturant, city)
    elif "show" in tokens and "yelp" in tokens and "review" in tokens:
        # get a random yelp review
        resturant = " ".join(tokens[tokens.index("of")+1: tokens.index("in")])
        city = " ".join(tokens[tokens.index("in")+1:])
        return yelp.getReview(resturant, city)
    elif "cuisine" in tokens:
        # get cuisine of resturant
        resturant = " ".join(tokens[tokens.index("is")+1: tokens.index("in")])
        city = " ".join(tokens[tokens.index("in")+1:])
        return yelp.getCategory(resturant, city)
    elif "expensive" in tokens:
        # get num. of yelp dollar signs
        resturant = " ".join(tokens[tokens.index("is")+1: tokens.index("in")])
        city = " ".join(tokens[tokens.index("in")+1:])
        return yelp.getPrice(resturant, city)
    elif "address" in tokens:
        # get address of resturant
        resturant = " ".join(tokens[tokens.index("of")+1: tokens.index("in")])
        city = " ".join(tokens[tokens.index("in")+1:])
        return yelp.getLocation(resturant, city)
    elif "phone" in tokens:
        # get phone number of resturant
        resturant = " ".join(tokens[tokens.index("of")+1: tokens.index("in")])
        city = " ".join(tokens[tokens.index("in")+1:])
        return yelp.getPhonNum(resturant, city)
    elif re.search(r'[+|\-|/|*|//]|module|integer division|exponent|bit shift|exclusive or', text):
        return numeric.arith_operation(text)
    elif re.search(r'true|false', text.lower()):
        return numeric.logical_operation(text)
    elif "dice" in text:
        return numeric.roll_dice(text)
    elif 'or' in text:
        return numeric.random_pick(text)
    else:
        return "I cannot understand your command"



def main():
    text = "How is the wind in London"
    text = "what is the phone number of taqueria santa cruz in san luis obispo"
    result_text = run_command(text)
    print(result_text)

    # print( run_command("create new tasks list"))
    # print( run_command("add pick up george from to football to my tasks list"))
    # #print( run_command("remove pick up george from to football from my tasks list"))
    # #print( run_command("clear tasks list"))
    # print( run_command("read from tasks list"))
    # print(run_command("delete tasks list"))

if __name__ == "__main__":
    main()