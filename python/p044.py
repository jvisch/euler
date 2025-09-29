def pantagonal(n):
    return (n * (3*n - 1)) // 2


def pentagonals():
    # Pn=n(3n−1)/2
    n = 1
    while True:
        yield pantagonal(n)
        n += 1


def is_pentagonal(value):
    for p in pentagonals():
        if p == value:
            return True
        if p > value:
            return False


def result():
    found = set()
    for a in pentagonals():
        found.add(a)
        for b in pentagonals():
            if b >= a:
                break
            if a - b in found:
                if is_pentagonal(a+b):
                    print(f'({a}, {b} -> {a-b})')
                    return (a, b)


if __name__ == '__main__':
    result()
