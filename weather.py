import requests
import json


def convert_city_name(name):
    return name.replace(" ", "%20")

def kelvinToCelsius(kelvin):
    return round(kelvin - 273.15)

def kelvinToFahrenheit(kelvin):
    return round(kelvin * 1.8 - 459.67)

def extract_temp(data):
    d = data["main"]
    return d["temp"], d["temp_min"], d["temp_max"]

def extract_wind(data):
    d= data["wind"]
    return d["speed"],d["deg"]

def get_data_object(city):
    city = convert_city_name(city)
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "eb865af37edb9395f146878f866fd270"
    url = base_url + "q=" + city + "&appid=" + api_key
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def get_current_weather(city, f=True, c=False):
    data = get_data_object(city)
    if data is not None:
        temp, low, high = extract_temp(data)
        if f:
            return "The temprature in " + city + " is currently " + str(kelvinToFahrenheit(temp)) + " degrees fahrenheit"
        elif c:
            return "The temprature in " + city + " is currently " + str(kelvinToCelsius(temp)) + " degrees celsius"
        else:
            return "The temprature in " + city + " is currently " + str(temp) + " degrees kelvin"
    else:
        return "An error occurred fetching the weather data"

def get_high_low(city, f=True, c=False):
    data = get_data_object(city)
    if data is not None:
        temp, low, high = extract_temp(data)
        if f:
            return "The high for today in " + city + " is " + str(
                kelvinToFahrenheit(high)) + " degrees fahrenheit and the low for today is " + str(
                kelvinToFahrenheit(low)) + " degrees fahrenheit"
        elif c:
            return "The high for today " + city + " is " + str(
                kelvinToCelsius(high)) + " degrees celsius and the low for today is " + str(
                kelvinToCelsius(low))+ " degrees celsius"
        else:
            return "The high for today in " + city + " is " + str(
                high) + " degrees kelvin and the low for today is " + str(
                low)+ " degrees kelvin"
    else:
        return "An error occurred fetching the weather data"

def degrees_to_cardinal(d):
    dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    directions = {"N": "North", "NNE": "North", "ENE":"North east", "E":"East", "ESE":"East", "SE":"South east", "SSE":"Southeast", "S": "South", "SSW":"South", "SW": "South west", "WSW": "South west","W": "West", "WNW": "West", "NW": "North West", "NNW": "North West"}
    ix = int(round((d + 11.25)/22.5))
    return directions[dirs[ix % 16]]

def get_wind(city):
    data= get_data_object(city)
    if data is not None:
        speed, deg = extract_wind(data)
        direction = degrees_to_cardinal(deg)
        return "The wind is "+ str(speed) + " miles per hour heading " + direction
    else:
        return "An error occurred fetching the wind data"



def main():
    city= "San Luis Obispo"
    print(get_wind(city))




if __name__ == "__main__":
    main()