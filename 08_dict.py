fname = input('Enter file name ')

try:
    fh = open(fname)
except:
    print('No Such File!')
    quit()

lst = list()
dc = dict()

for line in fh:
    if not line.startswith('From') or line.startswith('From:'): continue
    lst = line.split()
    dc[lst[1]] = dc.get(lst[1],0) + 1           #this is an important idiom to check for a key if it exists, we increment in its value, else we insert the new key and assign it default value '0'

bc = None
bw = None

for key,value in dc.items():
    if bc is None or value>bc:
        bw = key
        bc = value

print(bw,bc)
