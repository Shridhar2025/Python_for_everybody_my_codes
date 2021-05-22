import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('  Enter address ')
print('retrieving', address)

uh = urllib.request.urlopen(address)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)

lst = list()
sum=0
lst = info['comments']

for i in lst:
    sum = sum + i['count']

print(sum)
