from re import findall
import lame_menu as menu

yes = ("y","yes","ok","k","yeah","yah","sure","why not","of course")

def welcome():
    print("Welcome to weather app!\n")

def exit():
    print("Thanks for using the program, see u soon :)")

def show_weather(date_time, weather_data):
    for data in weather_data:
        if data["dt_txt"] == date_time:
            weather_data = data
            break
    print("The temperature now is "+str(weather_data["main"]["temp"]-273.15)+" degrees Celcius.")
    print("The minimum temperature is "+str(weather_data["main"]["temp_min"]-273.15)+" degrees Celcius.")
    print("The maximun temperature is "+str(weather_data["main"]["temp_max"]-273.15)+" degrees Celcius.")
    print("The humidity is "+str(weather_data["main"]["humidity"])+"%.")
    print("The wind speed is "+str(weather_data["wind"]["speed"])+" km/h.")
    print("We see "+str(weather_data["weather"][0]["description"])+".")


# Basic IO functions
def ask_input(item):
    while 1:
        try:
            user_input = input("Please enter "+item+":\n")
            return user_input
        except:
            show_error("Unexpected error")
            continue

def show_error(what_wrong):
    return print(what_wrong+", please try again.\n")

def show_done(done):
    return print("U have successfully "+done+".\n")

# Ask functions
def ask_country():
    while 1:
        country_name = ask_input("a country name")
        if len(findall(r"[a-zA-Z]", country_name)) > 0 and len(findall(r"[^a-zA-Z\s]", country_name)) == 0:
            return country_name
        error_country()

def ask_city():
    return ask_input("a city name")

def ask_back():
    if input("Would u like to go back to the menu though? (y or yes for yes and anything else for no)\n")\
       .lower() in yes:
        done_back()
        return True
    else:
        return False

def ask_continue():
    return ask_input("anything to continue")

# Error functions
def error_country():
    return show_error("The country name contains characters other than alphabets and spaces")

def error_no_results():
    return show_error("No results found")

# Done functions
def done_back():
    return show_done("gone back to the menu")

# Menus
def returns(item):
    return item

def country_menu(countries):
    cm = menu.Menu(after_num="for -->")
    cm.add_option("Exiting the program", returns, "exit")
    for country in countries:
        cm.add_option(country, returns, country)
    return cm.use()

def time_menu(times):
    tm = menu.Menu(after_num="for -->")
    tm.add_option("Changing Location", returns, "cl")
    tm.add_option("Exiting the program", returns, "exit")
    for time in times:
        tm.add_option(time, returns, time)
    return tm.use()