
# Name: {required}
# email:  {required}
# Assignment Number: Assignment nn  {required}
# Due Date:   {required}
# Course #/Section:   {required}
# Semester/Year:   {required}
# Brief Description of the assignment:  {required}
# Brief Description of what this module does. {Do not copy/paste from a previous assignment. Put some thought into this. required}
# Citations:
# Anything else that's relevant:

# api.py

import requests
import csv
from tabulate import tabulate

class OpenLibraryAPIHandler:
    @staticmethod
    def fetch_data(endpoint):
        """
        Builds the URL, sends a request to the Open Library API, and returns the JSON data.
        """
        base_url = "https://openlibrary.org/"
        url = f"{base_url}{endpoint}"  # Build the URL
        print(f"Built URL: {url}")

        # Submit the request and receive the results
        response = requests.get(url)
        if response.status_code == 200:
            print("API request successful.")
            return response.json()  # Parse the results into a Python dictionary
        else:
            print(f"API request failed with status code: {response.status_code}")
            return None

    @staticmethod
    def extract_data(json_data, title_wrap_length=45):
        """
        Extracts interesting information from JSON data, formats the title to wrap if too long, 
        and prints it in a friendly format.
        """
        extracted_data = []
        unique_entries = set()  # To track unique entries and avoid duplicates

        print("\nExtracted Book Data:\n")
        for book in json_data.get('docs', []):
            title = book.get('title', 'N/A')
            author = book.get('author_name', ['N/A'])[0]
            first_publish_year = book.get('first_publish_year', 'N/A')

            # Skip entries with 'N/A' for author or year
            if author == 'N/A' or first_publish_year == 'N/A':
                continue

            # Wrap the title if it's too long
            if len(title) > title_wrap_length:
                title = '\n'.join([title[i:i + title_wrap_length] for i in range(0, len(title), title_wrap_length)])

            # Create a unique key for deduplication
            entry_key = (title, author, first_publish_year)
            if entry_key not in unique_entries:
                unique_entries.add(entry_key)
                extracted_data.append([title, author, first_publish_year])  # Add as list for tabulate

        # Sort by "First Publish Year" (descending) only for printing
        sorted_data = sorted(extracted_data, key=lambda x: (x[2] != 'N/A', x[2]), reverse=True)

        # Print the sorted data with centered "First Publish Year" column
        print(tabulate(sorted_data, headers=["Title", "Author", "First Publish Year"], tablefmt="grid", colalign=("left", "left", "center")))

        # Return extracted data for potential further use (like saving to CSV)
        return [{'Title': entry[0], 'Author': entry[1], 'First Publish Year': entry[2]} for entry in extracted_data]

    @staticmethod
    def save_to_csv(data, filename):
        """
        Saves extracted data to a CSV file.
        """
        if not data:
            print("No data to save to CSV.")
            return

        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f"\nData saved to {filename} successfully.")
