import requests
from bs4 import BeautifulSoup
import os

# URL to scrape
url = "https://www.patpat.lk/property/land/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    print(soup.find_all)
    
   
else:
    print("Failed to retrieve the page")   