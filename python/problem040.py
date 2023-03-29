# copied from problem 39
def to_digits(value):
    digits = []
    while value > 0:
        digits.append(value % 10)
        value //= 10
    digits.reverse()
    return digits

def numbers(start=1):
    n = start
    while True:
        yield n
        n += 1

def all_digits():
    for n in numbers():
        for d in to_digits(n):
            yield d

def take(iter, n):
    return (next(iter) for _ in range(n))

def result():
    MAX = 6
    digits = list(take(all_digits(), 10**MAX))
    x = (digits[10**n - 1] for n in range(MAX))
    
    r = next(x)
    for p in x:
        r *= p

    return r


if __name__ == "__main__":
   r = result()
   print(r)