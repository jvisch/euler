from lib.primes import Primes
from lib.numbers import to_digits, from_digits
import collections
import itertools


def circulars(value):
    digits = collections.deque(to_digits(value))
    yield value
    for _ in range(1, len(digits)):
        digits.rotate(1)
        yield from_digits(digits)


def is_circular_prime(prime):
    # return all(Primes.is_prime(c) for c in circulars(prime))
    for c in circulars(prime):
        if not Primes.is_prime(c):
            return False
    return True


def circular_primes(m):
    primes = itertools.takewhile(lambda p: p < m, Primes.primes())
    primes = list(primes)

    return (p for p in primes if is_circular_prime(p))


x = list(circular_primes(1_000_000))
print(x)
print(len(x))
