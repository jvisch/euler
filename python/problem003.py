import math
import itertools

isPrime = lambda n: not any(p for p in range(2, int(math.sqrt(n)) + 1) if not n % p)


def isPrimeFunc(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def primes():
    p = 2
    while True:
        if isPrimeFunc(p):
            yield p
        p += 1


def primeFactors(n=600851475143):
    f = primes()
    p = next(f)
    while n > 1:
        while n % p == 0:
            yield p
            n = int(n / p)
        p = next(f)


def result(n=600851475143):
    return max(primeFactors(n))

if __name__ == '__main__':
    print(result())