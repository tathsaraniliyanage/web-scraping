import requests
from bs4 import BeautifulSoup

url='https://example.com/'

response = requests.get(url)

if response.status_code==200:
    
    soup = BeautifulSoup(response.text, 'html.parser')
    # title with tag
    print(soup.title)
    
    # title without tag
    print(soup.title.string)
    
    # h1 without tag
    print(soup.h1.string)
    
    # p without tag
    print(soup.p.string)
    
    # a with tag
    print(soup.a)
    
    # a without tag
    print(soup.a.string)
    
    # all
    tags = soup.find_all(['h1','p'])
    for tag in tags:
        print(tag.text.strip())
    
    print('----')
    
    # all paragraphs
    paragraphs=soup.find_all('p')
    for paragraph in paragraphs:
        print(paragraph.get_text())
    
else:
    print('error')



