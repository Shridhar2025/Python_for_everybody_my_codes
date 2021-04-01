test = "X-DSPAM-Confidence:    0.8475"

pos = test.find('0')
num = test[pos:]
num = float(num)

print(num)
