import model
import viewer

viewer.welcome()

def find_country():
    while 1:
        country = model.get_country(viewer.ask_country().strip())
        if country != False:
            break
        viewer.error_no_results()
    if len(country) > 1:
        country = country[viewer.country_menu(country.keys())]
    return country

def find_city(country):
    while 1:
        city = viewer.ask_city().strip()
        city_id = model.get_city_id(city, country)
        if city_id != False:
            return city_id
        viewer.error_no_results()
        if viewer.ask_back():
            return False

def find_weather(city_id):
    while 1:
        weather_data = model.get_weather(city_id)["list"]
        date_time = []
        for weather_time in weather_data:
            date_time.append(weather_time["dt_txt"])
        choice = viewer.time_menu(date_time)
        if choice == "cl":
            return None
        elif choice == "exit":
            return "exit"
        viewer.show_weather(choice, weather_data)

def start():
    while 1:
        country = find_country()
        if country == "exit":
            return None
        city_id = find_city(country)
        if city_id == False:
            continue
        if find_weather(city_id) == "exit":
            viewer.exit()
            return None

start()