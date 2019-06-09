#!/usr/bin/env python3
''' Main program. '''

from dbman import *

class weather:
    def __init__(self):
        print('''
        Hello. Welcome to WeatherMan!
        ''')
        self.search = input("Enter city name: ")



if __name__ == "__main__":
    vacation = weather()
    print(get_code(vacation.search))