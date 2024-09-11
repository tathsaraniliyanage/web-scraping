# import required libs
# url of the page of scrap 
# send the get request to the server
# print the scrap data

import requests 
from bs4 import BeautifulSoup

url='https://example.com/'

response = requests.get(url)

if response.status_code==200:
    # get all in html code
    print(response.text)
else:
    print('error')







