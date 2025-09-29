from lib.primes import Primes
from lib.numbers import numbers


def prime_factors(number):
    prime = Primes.primes()
    p = next(prime)
    while number != 1:
        if number % p == 0:
            yield p
            number = number // p
        else:
            p = next(prime)


def uniques(items):
    u = []
    for i in items:
        if i not in u:
            u.append(i)
    return u


def result(length=4):
    found = []
    for n in numbers(start=2):
        print(n)
        f = prime_factors(n)
        f = uniques(f)
        if len(f) == length:
            found.append(n)
            if len(found) == length:
                return found
        else:
            found.clear()


if __name__ == '__main__':
    print(result())
