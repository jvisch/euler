from lib.primes import Primes


def result(max=2_000_000):
    primes = Primes.primes()
    p = next(primes)
    total = 0
    while p < max:
        total += p
        p = next(primes)

    return total


print(result())
