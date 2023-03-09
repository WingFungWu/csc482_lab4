import nltk
import weather

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
    else:
        return "I cannot understand your command"



def main():
    text = "What are the highs and lows in San Luis Obispo"
    result_text = run_command(text)
    print(result_text)

if __name__ == "__main__":
    main()