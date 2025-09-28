from math import floor, log10
from lib import primes
import datetime


def truncates(value):
    nr_of_digits = floor(log10(value))
    for i in range(nr_of_digits, 0, -1):
        yield value // 10**i
        yield value % 10**i


def is_truncable_prime(value):
    return all(primes.Primes.is_prime(p) for p in truncates(value))


def result():
    found_truncatable_primes = []
    all_primes = primes.Primes.primes()
    while len(found_truncatable_primes) < 11:
        prime = next(all_primes)
        if prime > 9:
            if is_truncable_prime(prime):
                print(prime)
                found_truncatable_primes.append(prime)

    print(found_truncatable_primes)
    print(sum(found_truncatable_primes))


if __name__ == '__main__':
    start = datetime.datetime.now()
    result()
    end = datetime.datetime.now()
    print(end - start)
