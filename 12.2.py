import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# convert user input from str to int
count = int(input("Enter count:"))
position = int(input("Enter position:"))-1

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# init list
lst = []
tags = soup('a')

for i in range(count):
    link = tags[position].get('href', None)
    print("Retrieving:", link)
    lst.append(tags[position].contents[0])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[position].get('href', None)
print(lst[-1])
