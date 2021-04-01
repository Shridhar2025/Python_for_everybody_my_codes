fname = input('Enter the file name ')

try:
    fh = open(fname)
except:
    print('No such file!')
    quit()
lst = list()
count = 0
con = list()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From') or line.startswith('From:'): continue
    lst = line.split()
    con.append(lst[1])
    print(lst[1])
    count = count+1

print("There were", count, "lines in the file with From as the first word")
