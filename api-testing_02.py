# Created this just to mess around with API's and learn from them. I've messed around with API's on my iPhone shortcuts, but not inside Python..

import requests
import os
import shutil
import json
from datetime import datetime
from pprint import pprint
from dotenv import load_dotenv


## CONSTANTS ##
API_BASE = "http://api.weatherstack.com/current"

width, height = shutil.get_terminal_size()

def welcome():
    print("#" * width)
    print("|  Welcome to WeatherStack's API Service!  |".center(width, "#"))
    print("|  https://weatherstack.com  |".center(width, "#"))
    print("#" * width)
    print()
    usr_input = "Nashville"
    return usr_input

def get_api():
    load_dotenv()
    api_key = os.getenv("WEATHERSTACK_API_KEY")
    if not api_key:
        raise (RuntimeError("WEATHERSTACK_API_KEY not set - check your .env"))
    return api_key

def get_data(api_key, usr_input):

    params = {
        "access_key": api_key,
        "query": str(usr_input),
        "units": "f",
    }

    resp = requests.get(API_BASE, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    return data

def display_data(data):

    current = data["current"]
    location = data["location"]
    city = location["name"]
    country = location["country"]
    state = location["region"]
    lat = location["lat"]
    lon = location["lon"]
    local_time = location["localtime"]
    timezone = location["timezone_id"]
    current_temp = current["temperature"]
    conditions = current["weather_descriptions"][0]
    feels = current["feelslike"]
    sunrise = current["astro"]["sunrise"]
    sunset = current["astro"]["sunset"]

    dt = datetime.strptime(local_time, "%Y-%m-%d %H:%M")
    date = dt.strftime("%A, %B %d, %Y")
    time = dt.strftime("%I:%M%p")

    print("-" * width)
    print(f"{city}'s Weather".center(width))
    print(f"{country}, {state}".center(width))
    print(f"[ Latitude: {lat} ]---[ Longitude: {lon} ]".center(width))
    print("----------------------------------------------------".center(width))
    print(date.center(width))
    print(f"{time} {timezone}".center(width))
    print("-" * width)
    print()
    print(f"The current temperature is: {current_temp}F / Feels like: {feels}F")
    print(f"Weather conditions: {conditions}")
    print(f"Sunrise: {sunrise} // Sunset: {sunset}")
    print()
    print("-" * width)

def main():
    location = welcome()
    api_key = get_api()
    data = get_data(api_key, location)
    # print(json.dumps(data, indent=2))
    display_data(data)
    
if __name__ == "__main__":
    main()

