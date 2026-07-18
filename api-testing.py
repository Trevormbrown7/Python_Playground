# Created this just to mess around with API's and learn from them. I've messed around with API's on my iPhone shortcuts, but not inside Python..

import requests
import os
from pprint import pprint
from dotenv import load_dotenv


## CONSTANTS ##
API_BASE = "http://api.weatherstack.com/current"

def welcome():
    print("Welcome to WeatherStack's API Service!\nhttps://weatherstack.com/dashboard")
    usr_input = input("Location?\n")
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

    current = data["current"]
    location = data["location"]["name"]
    current_temp = current["temperature"]
    conditions = current["weather_descriptions"][0]
    feels = current["feelslike"]
    sunrise = current["astro"]["sunrise"]
    sunset = current["astro"]["sunset"]

    print("-" * 40)
    print(f"{location} Weather".center(40))
    print("-" * 40)
    print(f"The current temperature in {location} is: {current_temp}F / Feels like: {feels}F")
    print(f"Weather conditions: {conditions}")
    print(f"Sunrise: {sunrise} // Sunset: {sunset}")
    print("-" * 40)

    return data


def main():
    usr_input = welcome()
    api_key = get_api()
    get_data(api_key, usr_input)
    print("done")


if __name__ == "__main__":
    main()


"""So here's my nudge: what if you **split it into two boxes**?
One `get_data(api_key, location)` whose *only* job is to fetch and `return data` —
all those `print` lines move out. And a second function, something like `display_weather(data)`,
whose only job is to take `data` and print the report. Then `main()` becomes a beautifully
readable little story:

location = welcome()
api_key  = get_api()
data     = get_data(api_key, location)
display_weather(data)
hshshshs
shshshshsh
"""
