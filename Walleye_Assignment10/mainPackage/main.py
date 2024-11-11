#main.py

import json 
import requests

def JSONMod():
    response = requests.get('https://openlibrary.org/search.json?title=the+lord+of+the+rings')
    

