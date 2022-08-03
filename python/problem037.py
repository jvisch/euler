from math import floor, log, sqrt

found_primes = [2]


def primes():
    for p in found_primes:
        yield p
    p = found_primes[-1]
    while True:
        p += 1
        if not any(p % v == 0 for v in found_primes if v <= sqrt(p)):
            found_primes.append(p)
            yield p


def is_prime(value):
    if found_primes[-1] < sqrt(value):
        raise Exception(f"'{value} hasn't been checked yet")
    return value in found_primes


def truncates(value):
    nr_of_digits = floor(log(value, 10))
    for i in range(nr_of_digits, 0, -1):
        yield value // 10**i
        yield value % 10**i


def is_truncable_prime(value):
    return all(is_prime(p) for p in truncates(value))


def result():
    found_truncatable_primes = []
    all_primes = primes()
    while len(found_truncatable_primes) < 11:
        prime = next(all_primes)
        if prime > 9:
            if is_truncable_prime(prime):
                found_truncatable_primes.append(prime)

    print(found_truncatable_primes)
    print(sum(found_truncatable_primes))


if __name__ == '__main__':
    result()
