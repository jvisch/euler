def to_binary(value):
    while value > 0:
        yield value % 2
        value = value // 2 # int divisor

def is_palindrome(value):
    return value == value[::-1]

