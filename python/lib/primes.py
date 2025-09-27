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


def prime_factors(n=600851475143):
    f = Primes.primes()
    p = next(f)
    while n > 1:
        while n % p == 0:
            yield p
            n = int(n / p)
        p = next(f)
