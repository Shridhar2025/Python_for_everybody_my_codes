fname = input('Enter file name: ')

try:
    fh = open(fname)
except:
    print('No such file!')
    quit()

lst = list()
con = list()
ctr = 0

for line in fh:
    #print(line)
    line = line.rstrip()
    lst = line.split()
    for item in lst:
        if item not in con:
            con.append(item)
    # if ctr == 0:
    #     con = lst
    #     ctr = ctr+1
    # con.extend(lst)

fin = list()

# for item in con:
#     if item not in fin:
#         fin.append(item)
con.sort()                  # first sort the string list and then assign it to another list variable, else your data will get lost and print statement will show 'None'. this is because sort() modifies the original list
fin1 = list()
fin1 = con
print(fin1)
