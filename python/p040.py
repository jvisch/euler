# copied from problem 39
from lib.numbers import to_digits, numbers


def all_digits():
    return (d for n in numbers() for d in to_digits(n))


def take(iter, n):
    return (next(iter) for _ in range(n))


def result():
    MAX = 6
    digits = list(take(all_digits(), 10**MAX))
    x = (digits[10**n - 1] for n in range(MAX))

    r = next(x)
    for p in x:
        r *= p

    return r


if __name__ == "__main__":
    r = result()
    print(r)
