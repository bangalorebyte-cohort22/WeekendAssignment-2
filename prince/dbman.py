#!/usr/bin/env python3
''' Manages the database part '''

import json
import re

# Loading the json file (complete list of cities)
fin = open('databases/city.list.json', 'r')
db = json.load(fin)
fin.close()

def get_code(search):
    search = "".join(re.sub(r' +', ' ', search))
    search = search.strip().title()
    for places in db:
        if places['name'] == search:
            return places['id']

def parse_city_id(city_id):
    for cities in db:
        if cities['id'] == city_id:
            return cities['name']


if __name__ == "__main__":
    # search = input("Enter a city name:")
    response = get_code(input("Enter city name: "))
    
    if response:
        print("\nCity code is:",response)
    else:
        print("Not a valid city name. Try again.")
