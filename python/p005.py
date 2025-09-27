import p003
import itertools
import collections
import operator
import functools
from lib.primes import Primes


def result():
    allFactors = sorted(
        itertools.chain.from_iterable(allPrimeFactorsCount(20)))
    groupedFactors = itertools.groupby(allFactors, lambda x: x[0])
    maxFactors = [max(i[1]) for i in groupedFactors]
    almostTheResult = list(map(lambda n: n[0]**n[1], maxFactors))
    return functools.reduce(lambda a, b: a*b, almostTheResult)


def allPrimeFactorsCount(max):
    for n in range(2, max+1):
        yield factorsCount(n)


def primeFactors(n):
    primes = itertools.takewhile(lambda x: x <= n, Primes.primes())
    for p in primes:
        while n % p == 0:
            yield p
            n = n/p


def factorsCount(n):
    return collections.Counter(primeFactors(n)).most_common()


if __name__ == '__main__':
    print(result())
