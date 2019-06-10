import requests
import pandas as pd
import os
import json
import pyfiglet
from datetime import datetime
import time
import sys

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
os.chdir(THIS_FOLDER)

api_key_1 = "0e71adedcd098647c1ef46440888cb56"
api_key_2 = "d7a597fef845c4a34a8604a08a589a15"
api_key_3 = "1534719b67a41207d1af8b8c0fbde0d7"


def main_info(*args, **kwargs):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + initial_menu.city + "&appid=" + api_key_2 + "&units=metric"
    df = pd.DataFrame([requests.get(url).json()])
    df = df.reindex(['main'], axis=1)
    df = df.main.apply(pd.Series)
    tmin = df.iloc[0]['temp_min']
    tmax = df.iloc[0]['temp_max']
    humid = df.iloc[0]['humidity']
    main_info.humid_ = [humid]

    pressure = df.iloc[0]['pressure']
    avg_temp = df.iloc[0]['temp']

    main_info.tmin = tmin
    main_info.tmax = tmax
    main_info.pressure = pressure
    main_info.avg_temp = avg_temp


def avg_temp():
    print("Average Temp.: " + str(main_info.avg_temp))


def minmax():
    print(main_info.tmin, main_info.tmax)


def max_temp():
    print(main_info.tmax)


def misc_data():
    pass


def pressure():
    print(main_info.pressure)


def humid():

    print(main_info.humid_[0])


def quit():
    sys.exit()


def initial_menu():
    initial_heading = pyfiglet.figlet_format("Weather!")
    print(initial_heading)
    while True:
        try:
            city = input("Enter city name: ")
            initial_menu.city = city
            main_info()
            time.sleep(1)
            main_menu()

        except ValueError:
            print("Oops! Something went wrong. Please try again.")


def main_menu():
    os.system("clear")
    heading = pyfiglet.figlet_format(initial_menu.city)
    print(heading)

    while True:
        try:

            print('''
                      [1] -- > Find the Average Temperatures
                      [2] -- > Find the Minimum & Temperatures
                      [3] -- > Find Atmospheric Pressure
                      [4] -- > Find Humidity
                      [5] -- > Change City
                      [6] -- > Quit''')

            choice = int(input("[Enter]: "))

            #maps the options to their respective function
            menu_funcs = {
                1: avg_temp,
                2: minmax,
                3: pressure,
                4: humid,
                5: initial_menu,
                6: quit
            }
            if choice in menu_funcs:
                menu_funcs[choice]()  #calls the function

            else:
                print("Command not recognized. ")

        except ValueError:
            print("Please enter a number. ")


if __name__ == '__main__':
    initial_menu()
    main_info()
