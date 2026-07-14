# Created this just to mess around with API's and learn from them. I've messed around with API's on my iPhone shortcuts, but not inside Python..

import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHERSTACK_API_KEY")
if not api_key:
    raise (RuntimeError("WEATHERSTACK_API_LEY not set - check your .env"))



BASE = "http://api.weatherstack.com/current"

params = {
    "access_key": api_key,
    "query": "Nashville",
    "units": "f",
}

resp = requests.get(BASE, params=params)
data = resp.json()

print(json.dumps(data, indent=2))
current_temp = data["current"]["temperature"]

print(f"The current temperature in Nashville is: {current_temp}")
