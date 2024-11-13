#main.py

from apiPackage.api import OpenLibraryAPIHandler
 
if __name__ == "__main__":
    print("Starting the program")
 
    # Build the endpoint for searching the title "The Lord of the Rings"
    endpoint = "search.json?title=the+lord+of+the+rings"
    # Fetch data from the API
    api_handler = OpenLibraryAPIHandler()
    json_data = api_handler.fetch_data(endpoint)
 
    # If data was successfully fetched, process it
    if json_data:
        # Extract data using the existing method
        extracted_data = api_handler.extract_data(json_data)
        # Save the extracted data to a CSV file (if needed)
        api_handler.save_to_csv(extracted_data, "lord_of_the_rings_books.csv")
    else:
        print("No data to process.")
 
    print("Program completed")
has context menu


has context menu




'''
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
    '''

