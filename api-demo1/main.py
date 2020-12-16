import requests
import json

# Api key for accessing the API
ACCESS_KEY = "put_your_api_key"

# Input the City to fetch the weather
city = input('Enter the City to check the current weather: ')

# Call the Api endpoint by passing the API Key and the passing the City name
api_endpoint = "http://api.weatherstack.com/current?access_key=" + ACCESS_KEY + "&query=" + city

# Call the api using the requests.get() method
response = requests.get(api_endpoint)

# 
pretty_json = json.loads(response.text)

print(json.dumps(pretty_json, indent=2))
