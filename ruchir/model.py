from os import path
from os import chdir
from pandas.io.json import json_normalize

THIS_FOLDER = path.dirname(path.abspath(__file__))
chdir(THIS_FOLDER)

api_key_1 = "0e71adedcd098647c1ef46440888cb56"
api_key_2 = "d7a597fef845c4a34a8604a08a589a15"
api_key_3 = "1534719b67a41207d1af8b8c0fbde0d7"

def getWeather(city, units):
# Gets the weather data using just city name
    url = f"http://api.openweathermap.org/data/2.5/weather?q="{city}"&appid="{api_key_3}"&units="{units}
    df = pd.DataFrame([requests.get(url).json()])

def getWeatherSpecific(city, countryID, units):
# Get the specific user data of a particular city in a country. 
    url = f"http://api.openweathermap.org/data/2.5/weather?q="{city}","{countryID}"&appid="{api_key_3}"&units="{units}
    dfSpecific = pd.DataFrame([requests.get(url).json()])

def getWeatherZip(zipCode, countryID)
# Gets the weather data by zip/pin code
# If country is not specified then the search works for USA, by default
    url = f"http://api.openweathermap.org/data/2.5/weather?zip="{zipCode}","{countryID}"&appid="{api_key_3}"&units="{units}
    
def getForecast(city, countryID)
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{countryID}"

def getForecastZip(zipCode, countryID):
    url = f"http://api.openweathermap.org/data/2.5/forecast?zip={zipCode},{countryID}"
    
def getHourlyForecast(city, countryID):
    url = f"http://api.openweathermap.org/data/2.5/forecast/hourly?q={city},{countryID}"

    pass

def get16DayForecast(city, countryID)
    url = f"api.openweathermap.org/data/2.5/forecast/daily?id={city}&cnt={cnt}
    
def get16DayForecastZip(zipCode, countryID)
    url = f"http://api.openweathermap.org/data/2.5/forecast/daily?zip={zipCode},{countryID}


