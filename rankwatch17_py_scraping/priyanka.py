import urllib2
from bs4 import BeautifulSoup
boyNameWithA = "https://www.babynamesdirect.com/baby-names/indian/boy/a"

page = urllib2.urlopen(boyNameWithA)
soup = BeautifulSoup(page, "html5lib")

nameUl = soup.findAll("ul", { "class" : "nbd" })
print(nameUl)
