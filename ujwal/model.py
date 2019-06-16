import json
from requests import get

API_KEY = "80dbb4b24ec531115529d2d3b11abb80"

def get_country(country_name):
    country_info = get("https://restcountries.eu/rest/v2/name/"+country_name).json()
    if len(country_info) == 0 or type(country_info) == dict:
        return False
    countries = {}
    for i in country_info:
        countries[i["name"]] = i["alpha2Code"]
    return countries

def get_city_id(city_name,country_code):
    city_name = city_name.lower()
    cities = json.loads(open('city.list.min.json', encoding="utf-8").read())
    for city in cities:
        if city["name"].lower() == city_name and city["country"] == country_code:
            return city["id"]
    return False

def get_weather(city_id):
    weather_info = get("https://api.openweathermap.org/data/2.5/forecast?id="+str(city_id)+"&appid="+API_KEY).json()
    return weather_info