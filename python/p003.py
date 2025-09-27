from lib.primes import Primes, prime_factors




def result(n=600851475143):
    return max(prime_factors(n))


if __name__ == '__main__':
    print(result())
