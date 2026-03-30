# Write a program that fetches and prints out a random Chuck Norris joke for the user. Use the API presented here: https://api.chucknorris.io/. The user should only be shown the joke text.

import requests



request = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()

        print(json_response["value"])

except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")
