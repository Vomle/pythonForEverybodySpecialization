from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

url = 'https://www.dba.dk/soeg/?soeg=japan+bas&fra=privat'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))



x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')