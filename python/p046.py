import math

from lib.primes import Primes


def is_odd(number):
    return number % 2 == 1


def numbers(start=0, maximum=None):
    n = start
    while maximum is None or n < maximum:
        yield n
        n += 1


def check(number):
    for p in Primes.primes():
        if number - p < 2:
            return None
        else:
            square = math.sqrt((number - p) / 2)
            if square.is_integer():
                return (p, int(square))


def result():
    for n in numbers(start=2):
        if is_odd(n) and not Primes.is_prime(n):
            c = check(n)
            print(f'{n} -> {c}')
            if c is None:
                return n


if __name__ == '__main__':
    r = result()
    print(r)
