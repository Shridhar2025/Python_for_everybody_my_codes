from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
count = 0
l1 = list()

for tag in tags:
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    l1.append(int(tag.contents[0]))
    # print('Attrs:', tag.attrs)
    count = count+1

print('Count', count)
print(sum(l1))
