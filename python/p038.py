# De kleinste reeks is
#   1*getal = a
#   2*getal = b
#
#   "ab" aan elkaar zijn max 9 digits, dus getal is max 4 digits

from lib.numbers import from_digits, to_digits


def unique_values(items):
    for i in range(len(items) - 1):
        if items[i] in items[i+1:]:
            return False
    return True


def is_pandigital(value):
    if len(value) != 9:
        return False
    if 0 in value:
        return False
    return unique_values(value)


def result():
    # max 4 digits
    max = int(1e5)
    # range loops to max-1
    for getal in range(1, max):
        digits = to_digits(getal) + to_digits(2*getal)
        if len(digits) == 9:
            if is_pandigital(digits):
                yield from_digits(digits)
            elif len(digits) < 9:
                if not 0 in digits:
                    for p in [3, 4]:
                        digits += to_digits(p * getal)
                        if is_pandigital(digits):
                            yield from_digits(digits)


if __name__ == '__main__':
    for r in result():
        print(r)
