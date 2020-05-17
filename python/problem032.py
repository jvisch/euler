import itertools

digits = range(1, 8)  # 1..9


def get_items():
    for i in range(1, len(digits)+1):
        for c in itertools.combinations(digits, i):
            for p in itertools.permutations(c):
                yield set(p)


def get_combinations():
    i = 0
    items = list(get_items())
    for a in items:
        for b in items[i:]:
            if not any(item in a for item in b):
                yield (a, b)
        i = i+1


def to_digits(value):
    while not value == 0:
        yield value % 10
        value = int(value / 10)


def from_digits(digits):
    value = 0
    base = 1
    for d in digits:
        value = value + (base*d)
        base = base * 10
    return value


def is_pandigital(digits, length):
    if not len(digits) == length:
        return False
    items = sorted(digits)
    a = items[0]
    if not a == 1:
        return False
    for b in items[1:]:
        if not (b-a) == 1:
            return False
        a = b
    return True


def solve():
    total = 0
    for (a, b) in get_combinations():
        print(i)
        prod = from_digits(a) * from_digits(b)
        if is_pandigital(a + b + tuple(to_digits(prod)), len(digits)):
            print(from_digits(a))
            print(from_digits(b))
            print(prod)
            print()
            total = total + prod
    return total


# print(solve())

import time

start = time.time()
x = list(get_combinations())
end = time.time()
print(end - start)

print(len(x))