import requests
import json

API_KEY = 'd9981ef9'
title = input("Enter the movie to get the details: ")

response = requests.get('http://www.omdbapi.com/?apikey='+API_KEY+'&t='+title)

# Parse the response into JSON
parsed = json.loads(response.content)

# Dump the parsed JSON to indent and sort JSON on basis of keys
json_output = json.dumps(parsed, indent=4, sort_keys=True)

print(json_output)
