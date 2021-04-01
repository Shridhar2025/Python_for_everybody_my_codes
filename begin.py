hours = float(input('Enter Hours '))
rate = float(input('Enter rate per hour'))
if hours<=40:
    gpay = hours*rate
else:
    gpay = (40*rate)+((hours-40)*(rate*1.5))
print(gpay)
