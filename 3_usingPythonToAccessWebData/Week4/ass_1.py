from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1050112.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

nr_list = []
tags = soup('span')
for tag in tags:
    nr_string = tag.contents[0]
    nr_int = int(nr_string)
    nr_list.append(nr_int)

count = len(nr_list)
summ = sum(nr_list)

print("Count", count)
print("Sum", summ)
