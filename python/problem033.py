from fractions import Fraction

result = 1

for a in range(10, 100):
    for b in range(a+1, 100):  # only proper fractions ( a must be less then b )
        if a % 10 != 0 and b % 10 != 0: # trivial
            for x in str(a): # check any digit
                if x in str(b):
                    c = int(str(a).replace(x, '', 1))
                    d = int(str(b).replace(x, '', 1))
                    if d > 0:
                        e = Fraction(a,b)
                        f = Fraction(c,d)
                        if e == f:
                            print("{} / {} == {}".format(a, b, f))
                            result = result * e

print(result)
print("answer: {}".format(result.denominator))
