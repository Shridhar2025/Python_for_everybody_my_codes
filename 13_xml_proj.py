import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# api_key = False

# if api_key is False:
#     api_key = 42
#     serviceurl = 'https://py4e-data.dr-chuck.net/xml?'
# else:
#     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter address: ')
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
lst2 = list()
print('Count:', len(lst))

for item in lst:
    lst2.append(int(item.find('count').text))

print('Sum:', sum(lst2))
