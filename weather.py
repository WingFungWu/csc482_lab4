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
def main():
    city= "San Luis Obispo"
    print(get_high_low(city))




if __name__ == "__main__":
    main()