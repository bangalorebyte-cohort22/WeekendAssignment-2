#!/usr/bin/env python3
''' Manages the database part '''

import json
import re

# Loading the json file (complete list of cities)
fin = open('city.list.json', 'r')
db = json.load(fin)
fin.close()

# Query url
# url = ''
# "api_key = 'f5245c1537e27b43093b74ae91ff5d2d'\n",
#     "url = f'http://api.openweathermap.org/data/2.5/forecast?id=1277333&APPID={api_key}'\n"
def get_code(search):
    # Cleaning the user input.
    search = "".join(re.sub(r' +', ' ', search))
    search = search.strip().title()
    print(search)
    # Searching the db for city id.
    for places in db:
        if places['name'] == search:
            return places['id']


if __name__ == "__main__":
    # search = input("Enter a city name:")
    response = get_code(input("Enter city name!"))

    if response:
        print(response)
    else:
        print("Not a valid city name. Try again.")