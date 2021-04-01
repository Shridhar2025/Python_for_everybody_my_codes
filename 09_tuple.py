fname = input('Enter file name ')

try:
    fh = open(fname)
except:
    print('No such file!')
    quit()

lst = list()
lst2 = list()
dc = dict()


for line in fh:
    if not line.startswith('From') or line.startswith('From:'): continue
    lst = line.split()
    lst2 = lst[5].split(':')
    dc[lst2[0]] = dc.get(lst2[0],0) + 1

# print(dc)

# sorting the dictionary by hour

# lst3 = list()

for key,value in sorted(dc.items()):
    print(key,value)
