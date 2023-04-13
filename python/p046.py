import math


class Primes:
    n = 1
    pr = list()  # do not use set, a set is not ordered

    @classmethod
    def primes(c):
        for p in c.pr:
            yield p

        while True:
            c.n += 1
            for p in c.pr:
                if c.n % p == 0:
                    break
            else:
                c.pr.append(c.n)
                yield c.n

    @classmethod
    def is_prime(c, number):
        for p in c.primes():
            if p > number:
                return False
            elif p == number:
                return True


def is_odd(number):
    return number % 2 == 1


def numbers(start=0, max=None):
    n = start
    while max is None or n < max:
        yield n
        n += 1


def check(number):
    for p in Primes.primes():
        if number - p < 2:
            return None
        else:
            square = math.sqrt((number - p) / 2)
            if square.is_integer():
                return (p, int(square))

def result():
    for n in numbers(start=2):
        if is_odd(n) and not Primes.is_prime(n):
            c = check(n)
            print(f'{n} -> {c}')
            if c is None:
                return n

if __name__ == '__main__':
    r = result()
    print(r)
