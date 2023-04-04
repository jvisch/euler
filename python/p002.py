import itertools

_max = 4000000


def fibonacci():
    a, b = 1, 2
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


def result1():
    total = 0
    for i in itertools.takewhile(lambda n: n < _max, fibonacci()):
        if i % 2 == 0:
            total += i
    return total


def result2():
    numbers = [n for n in itertools.takewhile(lambda a: a < _max, fibonacci()) if n % 2 == 0]
    total = sum(numbers)
    return total


def result3():
    stop = lambda a: a < _max
    fibnumbers = itertools.takewhile(stop, fibonacci())
    iseven = lambda n: n % 2
    fibevennumbers = itertools.filterfalse(iseven, fibnumbers)
    return sum(fibevennumbers)
