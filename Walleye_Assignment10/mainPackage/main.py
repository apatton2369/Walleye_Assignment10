# Name: Alex Patton, Nandini Agarwal
# email:  pattona6@mail.uc.edu, agarwand@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   11/14/2024
# Course #/Section: IS 4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Execute an API call using a URL
# Brief Description of what this module does. This module fetches data from the API and extracts it. 
# Then the module converts that data into a CSV file.
# Citations:
# Anything else that's relevant:

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




