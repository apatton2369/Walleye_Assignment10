#main.py

import json 
import requests

def JSONMod():
    response = requests.get('https://openlibrary.org/search.json?title=the+lord+of+the+rings') # gets the API url
    json_string = response.content # recieves results from the URL
    parsed_json = json.loads(json_string) #parses the results into a python dictionary

    for firstSentance in parsed_json['docs']:
        print (firstSentance["first_sentence"][0]) 
        break

JSONMod()
    

