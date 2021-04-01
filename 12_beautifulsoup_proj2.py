import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

count = int(input('Enter Count '))
position = int(input('Enter position '))
ctr = 0

while (count > 0):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    ctr = 0
    for tag in tags:
        # print('Retrieving',tag.get('href', None))
        ctr = ctr+1
        if (ctr == position):
            print(tag.contents[0])
            url = str(tag.get('href', None))
            f = 1
    count = count-1
