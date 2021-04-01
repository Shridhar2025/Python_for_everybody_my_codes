largest = None
smallest = None
l1 = []

while True:
    num = input('Enter a number ')
    if num == 'done':
        for i in l1:
            if largest is None:
                largest = i
            elif i>largest:
                largest = i
        print('Maximum is',largest)

        for i in l1:
            if smallest is None:
                smallest = i
            elif i<smallest:
                smallest = i
        print('Minimum is',smallest)
        break
    #print(num)

    try:
        f = int(num)
        l1.append(f)
    except:
        print('Invalid input')
        continue



# print("Maximun",largest)
