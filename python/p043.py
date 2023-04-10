import itertools


def to_digits(value):  # copied from problem 38
    digits = []
    while value > 0:
        digits.append(value % 10)
        value //= 10
    digits.reverse()
    return digits


def from_digits(digits):  # copied from problem 38
    value = 0
    for d in digits:
        value = (value * 10) + d
    return value


def pandigitals():
    digits = to_digits(1234567890)
    for d in itertools.permutations(digits):
        if d[0] != 0:
            yield d


def pandigital_parts(digits):
    for start in range(1, len(digits)-2):
        yield digits[start:start+3]


def check(digits):
    parts = pandigital_parts(digits)
    # d2d3d4 deelbaar door 2
    p = next(parts)
    if p[-1] not in {0, 2, 4, 6, 8}:
        return False
    # d3d4d5 deelbaar door 3
    p = next(parts)
    if not sum(p) % 3 == 0:
        return False
    # d4d5d6 deelbaar door 5
    p = next(parts)
    if not (p[-1] == 0 or p[-1] == 5):
        return False
    # d5d6d7 deelbaar door 7
    p = next(parts)
    if not from_digits(p) % 7 == 0:
        return False
    # d6d7d8 deelbaar door 11
    p = next(parts)
    if not from_digits(p) % 11 == 0:
        return False 
    # d7d8d9 deelbaar door 13
    p = next(parts)
    if not from_digits(p) % 13 == 0:
        return False
    # d8d9d10 deelbaar door 17
    p = next(parts)
    if not from_digits(p) % 17 == 0:
        return False
    # done
    return True

def result():
    total = 0
    for digits in pandigitals():
        if check(digits):
            number = from_digits(digits)
            print(number)
            total += number
    print(total)

if __name__ == '__main__':
    result()