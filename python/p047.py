import p046


# def is_consecutive(values):
#     values = list(values)
#     if len(values) <= 1:
#         return True
#     else:
#         if values[1] - values[0] == 1:
#             return is_consecutive(values[1:])
#         else:
#             return False

# numbers = 3 * (None,)

# for i in p046.numbers(2, 1000):
#     c = (i, p046.check(i))
#     numbers = numbers[1:] + (c,)
#     if not None in numbers:
#         values = (i for i, c in numbers)
#         primes = (c for i, c in numbers if c is not None)
#         unique_primes = {prime for prime, _ in primes}
#         if len(unique_primes) == len(numbers):
#             if is_consecutive(values):
#                 # found it
#                 print(numbers)

def prime_factors(number):
    prime = p046.Primes.primes()
    p = next(prime)
    while number != 1:
        if number % p == 0:
            yield p
            number = number // p
        else:
            p = next(prime)

def uniques(items):
    u = []
    for i in items:
        if i not in u:
            u.append(i)
    return u


def result(length=4):
    found = []
    for n in p046.numbers(start=2):
        print(n)
        f = prime_factors(n)
        f = uniques(f)
        if len(f) == length:
            found.append(n)
            if len(found) == length:
                return found
        else:
            found.clear()

if __name__ == '__main__':
    print(result())