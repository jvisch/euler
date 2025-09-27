from lib.primes import Primes


def quadratic_formula(a, b, n):
    return (n*n) + (a*n) + b


def quadratic_prime(a, b, n):
    q = quadratic_formula(a, b, n)
    p = Primes.is_prime(q)
    return p, q


def quadratics(a, b):
    lst = []
    n = 0
    p, q = quadratic_prime(a, b, n)
    while p:
        lst.append(q)
        n += 1
        p, q = quadratic_prime(a, b, n)
    return a, b, lst


m = 1000
items = [quadratics(a, b) for a in range(-m+1, m+1) for b in range(-m+1, m+1)]
item = max(items, key=lambda item: len(item[2]))

result = item[0] * item[1]

print(result)
