import requests
import pandas as pd
import os
import json
import pyfiglet
from datetime import datetime
import time
import sys
from terminaltables import AsciiTable

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
os.chdir(THIS_FOLDER)

api_key_1 = "0e71adedcd098647c1ef46440888cb56"
api_key_2 = "d7a597fef845c4a34a8604a08a589a15"
api_key_3 = "1534719b67a41207d1af8b8c0fbde0d7"


def main_info(*args, **kwargs):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + initial_menu.city + "&appid=" + api_key_2 + "&units=metric"
    df = pd.DataFrame([requests.get(url).json()])
    query = "city not found"
    # if query in df:
    #     print("City name does not exist. Please try again.")
    try:
        df = df.reindex(['main'], axis=1)
        df = df.main.apply(pd.Series)
        tmin = df.iloc[0]['temp_min']
        tmax = df.iloc[0]['temp_max']
        humid = df.iloc[0]['humidity']
        pressure = df.iloc[0]['pressure']
        avg_temp = df.iloc[0]['temp']
        wind = df.iloc[0]['wind']
        
        df = df.coord.apply(pd.Series)
        longitude = df.iloc[0]['coord']
        latitude - df.iloc[0]['coord']
        
        df = df.weather.apply(pd.Series)
        main_weather = df.iloc[0]['Main']
    except:
        print("City name does not exist. Please try again.")
        initial_menu()
    
    title = initial_menu.city.capitalize()+"'s Weather"
    
    weather_data = [
        []
    ]
    
    table_data = [
        ["City","Min", "Max","Humidity", "Pressure", 'Avg. Temp.'],
        [initial_menu.city.capitalize(), tmin, tmax, humid, pressure, avg_temp]
    ]
    
    table = AsciiTable(table_data, title)
    print (table.table)


def quit():
    sys.exit()


def initial_menu():
    initial_heading = pyfiglet.figlet_format("Weather!")
    print(initial_heading)
    while True:
        try:
            city = input("Enter city name: ")
            initial_menu.city = city
            # main_info()
            time.sleep(1)
            change_city()

        except ValueError:
            print("Oops! Something went wrong. Please try again.")
            
#//TODO: Include ability to search by zip code as well
#//TODO: Ask for country name as well
#//TODO: Map country codes to country name
#// TODO: Connect the Quit option
#//TODO: Have the option of changing to imperial
#//TODO: Download and parse that JSON with Pandas and look with a loop if the city & country the user entered is in the weather API list

def change_city():
    os.system("clear")
    heading = pyfiglet.figlet_format(initial_menu.city.capitalize())
    print(heading)
    main_info()
    print('''
          [1] Change City
          [2] Quit''')
    
    input_ = input("[Enter]: ")
    if input_ == '1':
         initial_menu()
    elif input_ == '2':
        sys.exit()
    # elif input_ = 
         

    # while True:
    #     try:

    #         print('''
    #                   [1] -- > Find the Average Temperatures
    #                   [2] -- > Find the Minimum & Temperatures
    #                   [3] -- > Find Atmospheric Pressure
    #                   [4] -- > Find Humidity
    #                   [5] -- > Change City
    #                   [6] -- > Quit''')

    #         choice = int(input("[Enter]: "))

    #         #maps the options to their respective function
    #         menu_funcs = {
    #             1: avg_temp,
    #             2: minmax,
    #             3: pressure,
    #             4: humid,
    #             5: initial_menu,
    #             6: quit
    #         }
    #         if choice in menu_funcs:
    #             menu_funcs[choice]()  #calls the function

    #         else:
    #             print("Command not recognized. ")

    #     except ValueError:
    #         print("Please enter a number. ")


if __name__ == '__main__':
    initial_menu()
    # main_info()
