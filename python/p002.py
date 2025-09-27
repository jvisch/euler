import itertools
from lib.numbers import fibonacci

MAX = 4000000


def result1():
    total = 0
    for i in itertools.takewhile(lambda n: n < MAX, fibonacci()):
        if i % 2 == 0:
            total += i
    return total


def result2():
    numbers = [n for n in itertools.takewhile(
        lambda a: a < MAX, fibonacci()) if n % 2 == 0]
    total = sum(numbers)
    return total


def result3():
    def stop(a): return a < MAX
    fibnumbers = itertools.takewhile(stop, fibonacci())
    iseven = lambda n: n % 2
    fibevennumbers = itertools.filterfalse(iseven, fibnumbers)
    return sum(fibevennumbers)

results = [result2(), result2(), result3()]

for r in results:
    print(r)