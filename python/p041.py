import itertools
import math
from lib.numbers import to_digits, from_digits
from lib.primes import Primes

def is_pandigital(value):
    digits = sorted(value)
    a = digits[0]
    for i in range(1, len(digits)):
        b = digits[i]
        if b-a > 1:
            return False
    return True


def pandigital_numbers():
    digits = to_digits(123456789)
    for n in range(1, 9):
        for g in itertools.permutations(digits[:-n]):
            # deelbaar door 2 of door 5?
            if g[-1] not in {0, 2, 4, 5, 6, 8}:
                if sum(g) % 3 != 0:
                    yield from_digits(g)


def pandigital_prime_numbers():
    pandigitals = sorted(pandigital_numbers())

    for n in pandigitals:
        if Primes.is_prime(n):
            yield n


if __name__ == '__main__':
    for n in pandigital_prime_numbers():
        print(n)
