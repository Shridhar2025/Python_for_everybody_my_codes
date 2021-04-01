hours = float(input('Enter Hours '))
rate = float(input('Enter rate per hour '))

def computepay(hrs,r):
    if hrs<=40:
        gpay = hrs*r
    else:
        gpay = (40*r)+((hrs-40)*(r*1.5))
    return gpay



p = computepay(hours,rate)
print("Pay",p)
