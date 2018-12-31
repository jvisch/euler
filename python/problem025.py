import math

a=1
b=1

i=2

nDigits = 1000

while math.floor(math.log10(b)) + 1 < nDigits :
    a, b = b, a+b
    i+=1
    print(i, b)


