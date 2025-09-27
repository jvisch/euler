import math


def result(n=100):
    return sum([int(i) for i in str(math.factorial(n))])

print(result())