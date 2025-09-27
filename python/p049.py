from lib.primes import Primes
import p041
import itertools


def primes():
    primes = Primes.primes()
    p = next(primes)
    while p < 10000:
        if p > 1000:
            print(p)
            yield p
        p = next(primes)


def are_permutations(numbers):
    iter_numbers = iter(numbers)
    first = next(iter_numbers)
    key = sorted(p041.to_digits(first))
    for i in iter_numbers:
        if not key == sorted(p041.to_digits(i)):
            return False
    # All checks true
    return True


VALUE = 3330
# all primes + 3330 , + 2 x 3330
result = [(p, p + VALUE, p + VALUE + VALUE) for p in primes()]
# filter none primes
result = ((p1, p2, p3) for p1, p2, p3 in result if Primes.is_prime(p2) and Primes.is_prime(p3))
# check for permutation
result = (p for p in result if are_permutations(p))


for r in result:
    print(r)
    all_digits = [d for n in r for d in p041.to_digits(n)]
    the_real_result = p041.from_digits(all_digits)
    print(the_real_result)
