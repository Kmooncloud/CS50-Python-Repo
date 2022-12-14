import requests
import sys
import json

# Use the Itunes API and get information

if len(sys.argv) != 2:
    sys.exit()  # terminates the entire program 

# pretend to be a webbrowser to access an API
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))    # prints out formatted content of the response
o = response.json()
for result in o["results"]:
    print(result["trackName"])