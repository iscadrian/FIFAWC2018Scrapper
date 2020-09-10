import requests
from bs4 import BeautifulSoup

fifa_page = 'https://www.fifa.com/worldcup/groups/'
resp = requests.get(fifa_page)
soup = BeautifulSoup(resp, 'html.parser')


name_box = soup.find('h1', attrs={'class': 'fi-pageheader__title'})

name = name_box.text.strip()

print(name)
