#!/usr/bin/env python3
''' Main program. '''

import dbman
import requests
import json
import datetime

class weather:
    def __init__(self):
        self.city_id = 1277333 # 583509
        self.today = datetime.date.today()
        self.weather_data = self.get_data(self.city_id)
        self.selected_city = dbman.parse_city_id(self.city_id)
    
    def get_data(self, city_id):
        response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?id={self.city_id}&APPID=f5245c1537e27b43093b74ae91ff5d2d')
        weather_data = json.loads(response.content)['list']
        return weather_data
    
    def pick_data(self):
        pass

    def change_city(self):
        city_name = input("Enter city name: ")
        temp_id = dbman.get_code(city_name)
        if temp_id:
            self.city_id = temp_id
            self.selected_city = dbman.parse_city_id(self.city_id)
            main_menu()
            
        else:
            print(f'\n"{city_name}" does not exist. PLease try again. \nEnter q to quit.\n')
            main_menu()

    def overview(self):
        # print(json.dumps(self.weather_data, indent=4))
        for dates in self.weather_data:
            if dates['dt_txt'].startswith(str(self.today)):
                print(dates['weather'])
    

def main_menu():
    print(f'''\nCurrent city: {vacation.selected_city} \n
What do you want to do? \n1. Change city. \n2. Display overview (Today).\n3. Quit.''')
    main_input = input(">> ")
    
    if main_input == '1':
        vacation.change_city()

    elif main_input == '2':
        vacation.overview()

    elif main_input in ['3', 'q', 'Q', 'Quit', 'quit']:
        print('Logged out')

    else:
        print("invalid input. Try again.")
        main_menu()





if __name__ == "__main__":
    vacation = weather() 
    main_menu()
    # vacation = weather()
    # print(get_code(vacation.search))
    # print(json.dumps(vacation.weather_data))