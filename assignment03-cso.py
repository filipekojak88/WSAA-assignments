# This program retrieves the dataset for the "exchequer account (historical series)" from the CSO,
# and stores it into a file called "cso.json"
# Author: Filipe Carvalho

import requests
import json

# URL of the dataset from the CSO API
URL = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

def fetch_url(url):   
    # Fetches JSON data from the given URL
    response = requests.get(url)
    return response.json()

def store_file(url, filename="cso.json"):
    # Stores fetched data in a JSON file
    data = fetch_url(url)
    with open(filename, "wt") as fp:
        # Write JSON data to file
        json.dump(data, fp)  
    print(f"Data has been stored successfully in {filename}")

if __name__ == "__main__":
    # Pass the URL to the function
    store_file(URL)