from problem010 import primes2
from problem034 import to_digits
from math import sqrt, log10

MAX = 10**6
primes = set(p for p in primes2(MAX))


def is_prime(value):
    return value in primes


def to_number(digits):
    result = 0
    factor = 1
    for i in digits:
        result = result + i * factor
        factor = factor * 10
    return result


def get_circulars(value):
    nr_of_digits = int(log10(value))
    for _ in range(0, nr_of_digits+1):
        yield value
        value = int(value / 10) + ((value % 10) * 10**nr_of_digits)


def is_circular_prime(value):
    return all(is_prime(v) for v in get_circulars(value))


if __name__ == "__main__":
    result = [p for p in primes if is_circular_prime(p)]
    print("answer: {}".format(len(result)))
