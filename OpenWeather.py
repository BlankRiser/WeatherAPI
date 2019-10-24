import requests
import configparser
import pandas as pd

# remember to hide the API Key
apiKey = 'Inser your API Key here'

# Using configparser to get the API Key


cityName = input("Enter city name: ")


response = requests.get(
    "http://samples.openweathermap.org/data/2.5/weather?q=" + cityName + "&appid="+apiKey)

jsonData = response.json()

'''
#bangalore ID

{
    'coord': {'lon': -0.13, 'lat': 51.51}, 
    'weather': [{'id': 300, 'main': 'Drizzle', 'description': 'light intensity drizzle', 'icon': '09d'}], 
    'base': 'stations',
    'main': {'temp': 280.32, 'pressure': 1012, 'humidity': 81, 'temp_min': 279.15, 'temp_max': 281.15},
    'visibility': 10000,
    'wind': {'speed': 4.1, 'deg': 80},
    'clouds': {'all': 90},
    'dt': 1485789600, 
    'sys': {'type': 1, 'id': 5091, 'message': 0.0103, 'country': 'GB', 'sunrise': 1485762037, 'sunset': 1485794875},
    'id': 2643743,
    'name': 'London',
    'cod': 200
} 
'''
tempKel = jsonData['main']['temp']
tempCel = tempKel - 273.15

mintempKel = jsonData['main']['temp_min']
tempCel = mintempKel - 273.15

maxtempKel = jsonData['main']['temp_max']
tempCel = maxtempKel - 273.15

humidity = jsonData['main']['humidity']
pressure = jsonData['main']['pressure']

print("Temperature of ", cityName, ": ", tempCel,
      " Celcius or ", tempKel, " Kelvin")

print("Humidity: ", humidity, " percent")

print("Pressure: ", pressure)
