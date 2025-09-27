import math

from lib.primes import Primes as priemen


def is_odd(number):
    return number % 2 == 1


def numbers(start=0, max=None):
    n = start
    while max is None or n < max:
        yield n
        n += 1


def check(number):
    for p in priemen.primes():
        if number - p < 2:
            return None
        else:
            square = math.sqrt((number - p) / 2)
            if square.is_integer():
                return (p, int(square))

def result():
    for n in numbers(start=2):
        if is_odd(n) and not priemen.is_prime(n):
            c = check(n)
            print(f'{n} -> {c}')
            if c is None:
                return n

if __name__ == '__main__':
    r = result()
    print(r)
