import requests # you need this module to make an API call
import pandas as pd

OWM_API_KEY = "b140e402bed7f4f97188bc1e3e049034"
CURRENT_WEATHER_FILE = "currentweather.csv"
FORECAST_WEATHER_FILE = "currentforecast.csv"

api_url="http://api.openweathermap.org/data/2.5/weather?q=4166195&APPID=b140e402bed7f4f97188bc1e3e049034&units=imperial

payload={"APPID":OWN_API_KEY,"units":"imperial","q":4166195}

r=requests.get(api_url,params=payload)

r.url
print(r.request.body)
