
def fibonacci():
    a, b = 1, 2
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


def to_digits(value):
    digits = []
    while value > 0:
        d = value % 10
        digits.insert(0, d)
        value //= 10
    return digits   

def from_digits(digits):
    result = 0
    for i in digits:
        result = (result * 10 + i)
    return result


def factorial(value):
    if value <= 1:
        return 1
    return value * factorial(value-1)
