#!/usr/bin/env python3
''' Manages the database part '''

import json
import re

# Loading the json file (complete list of cities)
fin = open('databases/city.list.json', 'r')
db = json.load(fin)
fin.close()

def get_code(search):                                  # For getting city id.
    search = "".join(re.sub(r' +', ' ', search))
    search = search.strip().title()
    for places in db:
        if places['name'] == search:
            return places['id']

def parse_city_id(city_id):                            # Getting city name from the db.
    for cities in db:
        if cities['id'] == city_id:
            return cities['name']

def print_data(dates):                                 # Output format for the data.
    print('Time       :', dates['dt_txt'][-8:-1])
    print('Temp max   :', "{0:.2f}".format(dates['main']['temp_max']-273.15),'Celcius')
    print('Temp min   :', "{0:.2f}".format(dates['main']['temp_min']-273.15),'Celcius')
    print('Windspeed  :', dates['wind']['speed'],'mph')
    print('Humidity   :', dates['main']['humidity'],'%')
    print('Cloudiness :', dates['weather'][0]['description'])
    print('\n')


if __name__ == "__main__":
    response = get_code(input("Enter city name: "))    
    if response:
        print("\nCity code is:",response)
    else:
        print("Not a valid city name. Try again.")
