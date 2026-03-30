# Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api. Your task is to write a program that asks the user for the name of a municipality and then prints out the corresponding weather condition description text and temperature in Celsius degrees. Take a good look at the API documentation. You must register for the service to receive the API key required for making API requests. Furthermore, find out how you can convert Kelvin degrees into Celsius.

import requests

from api_key import api_key as api_key

municipality = input("Write your municipality")

request = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}"

try:
    response=requests.get(request)
    if response.status_code==200:
        json_response = response.json()

        kelvin=json_response["main"]["temp"]
        celsius= kelvin - 273.15

        print(f"The weather data are {json_response["weather"][0]["description"]}")
        print(f"The actual temperature is {celsius:.2f}")


except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")