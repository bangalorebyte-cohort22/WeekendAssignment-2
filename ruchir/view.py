from os import path
from os import chdir
from model import *

def asciitables():
    sun_table = AsciiTable(table_data, sun_title)
    wind_table = AsciiTable(wind_data, wind_title)
    main_table = AsciiTable(main_data, main_title)
    print(sun_table.table)
    print(wind_table.table)
    print(main_table.table)
