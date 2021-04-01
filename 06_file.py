fname = input('Enter the file name ')

try:
    fh = open(fname)
except:
    print('No such file!')
    quit()

for line in fh:
    line = line.rstrip()
    print(line.upper())
