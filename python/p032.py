def is_pandigital(value):
    if len(value) != 9:
        return False
    for i in range(1, 10):
        if not str(i) in value:
            return False
    return True


def solve():
    result = set()  # a set, don't count same products twice....
    for a in range(1, 100000):
        for b in range(a, 10000):
            product = a*b
            # string to check
            to_check = str(a)+str(b)+str(product)
            if len(to_check) > 9:  # if total is above max lenght (it will never be shorter)
                break
            if is_pandigital(to_check):
                print("{} x {} = {}".format(a, b, product))
                result.add(product)
    return sum(result)

print(solve())