#!/usr/bin/env python3
''' Main program. '''

import os
import re
import datetime
import json
import requests
import dbman
import menuman


class Weather:
    ''' For creating the weather class '''
    def __init__(self):
        self.city_id = 1277333 # 583509
        self.today = datetime.date.today()
        self.weather_data = self.get_data(self.city_id)
        self.selected_city = dbman.parse_city_id(self.city_id)

    def get_data(self, city_id):
        ''' Collects the weather data from the api in json format. '''
        response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?id={self.city_id}&APPID=f5245c1537e27b43093b74ae91ff5d2d')
        weather_data = json.loads(response.content)['list']
        return weather_data

    def change_city(self):
        ''' Selecting a different city. '''
        city_name = input("Enter city name: ")
        temp_id = dbman.get_code(city_name)
        if temp_id:
            self.city_id = temp_id
            self.selected_city = dbman.parse_city_id(self.city_id)
            self.weather_data = self.get_data(self.city_id)
            main_menu()

        else:
            print(f'\n"{city_name}" does not exist. PLease try again. \nEnter q to quit.\n')
            main_menu()

    def overview(self):
        ''' Printing the overview for that day. '''
        for dates in self.weather_data:
            if dates['dt_txt'].startswith(str(self.today)):
                print(f'\nToday\'s weather overview of {self.selected_city}.\n')
                dbman.print_data(dates)

    def advanced_search(self):
        ''' The advanced search function. '''
        self.today = datetime.date.today()
        days = input(f'{menuman.DAYS}>>> ')

        if days == '0':
            pass
        elif days == '1':
            self.today = self.today + datetime.timedelta(days=1)
        elif days == '2':
            self.today = self.today + datetime.timedelta(days=2)
        elif days == '3':
            self.today = self.today + datetime.timedelta(days=3)
        elif days == '4':
            self.today = self.today + datetime.timedelta(days=4)
        elif days == '5':
            print("Logged out")
            os._exit(0)
        else:
            print('Invalid option. Try again.')
            self.advanced_search()

        hours = input(f'{menuman.HOURS}>>> ')
        # For filtering out non digit characters
        hours_1 = re.sub(r'[^\d]', '', hours)
        x_x = len(hours)
        y_y = int(hours)
        if hours_1 != hours:
            print('\nPlease only enter numbers. Try again')
            self.advanced_search()

        # Parsing somewhat valid user input.
        if x_x > 0 and x_x < 3 and y_y == 24 and int(days) == 4:
            print('Search parameter exceeds 5 days. Try again')    # You cannot go more than 4 days.
            self.advanced_search()
        elif x_x > 0 and x_x < 3 and y_y == 24 and int(days) != 4:
            self.today = self.today + datetime.timedelta(days=1)   # Adding one more day if hours enteres is 24.
            print(self.today)
        elif x_x > 0 and x_x < 3 and y_y >= 0 and y_y < 24:
            self.selected_hour = y_y
        else:                                                      # Self explanatory. lol
            print('Our planet uses 24 hour clock.\nMr Alien, please enter an hour according to our clocks.')
            self.advanced_search()


        # Printing out data for valid queries.
        for dates in self.weather_data:
            x_x = self.selected_hour - int(dates['dt_txt'].split(" ")[1].split(":")[0])
            y_y = int(dates['dt_txt'].split(" ")[1].split(":")[0])
            if dates['dt_txt'].startswith(str(self.today)) and x_x == 0:
                print('###########################\nSelected hour is in this time window:')
                dbman.print_data(dates)
                break
            elif dates['dt_txt'].startswith(str(self.today)) and x_x < 3 and x_x > 0:
                print('###########################\nSelected hour is in this time window:')
                dbman.print_data(dates)
                break
            elif dates['dt_txt'].startswith(str(self.today)) and y_y >= 21 and x_x < 4:
                print('###########################\nSelected hour is in this time window:')
                dbman.print_data(dates)
            # elif dates['dt_txt'].startswith(str(self.today)) and i == len(self.weather_data):
            #     print('###########################\nSelected hour is is already passed.\nTry again.')
            #     self.advanced_search()

        # Return option.
        advanced_input = input(menuman.ADVANCED_INPUT)
        if advanced_input == '1':
            main_menu()
        elif advanced_input == '2':
            print('\nLogged out.')
            os._exit(0)
        else:
            print('\nInvalid input. Returning to main menu.\n')
            main_menu()


def main_menu():
    ''' Main menu '''
    print(f'''\n###########################\nCurrent city: {VACATION.selected_city} \n
What do you want to do? \n1. Change city. \n2. Display overview (Today).\n3. Advanced Search.\n4. Quit.''')
    main_input = input(">> ")

    if main_input == '1':
        VACATION.change_city()

    elif main_input == '2':
        overview_menu()

    elif main_input == '3':
        VACATION.advanced_search()

    elif main_input in ['4', 'q', 'Q', 'Quit', 'quit']:
        print('Logged out')
        os._exit(0)

    else:
        print("invalid input. Try again.")
        main_menu()

def overview_menu():
    ''' Overview menu '''
    VACATION.overview()
    overview_input = input("1. Go Back.\n2. Quit\n>> ")
    if overview_input == '1':
        main_menu()
    elif overview_input in ['2', 'q', 'Q', 'Quit', 'quit']:
        print("Logged out")
        os._exit(0)
    else:
        overview_menu()

if __name__ == "__main__":
    VACATION = Weather()
    main_menu()
