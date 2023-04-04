import itertools
import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_pandigital(value):
    digits = sorted(value)
    a = digits[0]
    for i in range(1, len(digits)):
        b = digits[i]
        if b-a > 1:
            return False
    return True


def to_digits(value):  # copied from problem 38
    digits = []
    while value > 0:
        digits.append(value % 10)
        value //= 10
    digits.reverse()
    return digits


def from_digits(digits):  # copied from problem 38
    value = 0
    for d in digits:
        value = (value * 10) + d
    return value


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
        if is_prime(n):
            yield n


if __name__ == '__main__':
    for n in pandigital_prime_numbers():
        print(n)
