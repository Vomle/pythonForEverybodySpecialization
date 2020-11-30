import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 7
position = 18
url = 'http://py4e-data.dr-chuck.net/known_by_Windsor.html'
print("Retrieving:", url)

# Retrieve all of the anchor tags

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position - 1].get('href', None)
    print("Retrieving:", url)

name = re.search('known_by_(.+)\.html', url).group(1)
print(name)
