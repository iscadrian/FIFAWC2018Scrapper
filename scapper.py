import urllib2
from bs4 import BeautifulSoup

fifa_page = 'https://www.fifa.com/worldcup/groups/'
req = urllib2.Request(fifa_page, headers={'User-Agent' : "Magic Browser"})
fifa_soup = urllib2.urlopen(req)
soup = BeautifulSoup(fifa_soup, 'html.parser')


name_box = soup.find('h1', attrs={'class': 'fi-pageheader__title'})

name = name_box.text.strip()

print name
