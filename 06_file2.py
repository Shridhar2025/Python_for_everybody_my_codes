fname = input('Enter the file name ')

try:
    fh = open(fname)
except:
    print('No such file!')
    quit()
count=0
f=0
asc=0

for line in fh:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'): continue
    #print(line)
    count = count+1
    f = float(line[19:])
    asc = asc+f

print('Average spam confidence:',asc/count)
