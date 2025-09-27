def nextCollatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1


def collatzSequence(n):
    while n > 1:
        yield n
        n = int(nextCollatz(n))
    yield 1


def sequenceLen(seq):
    cnt = 0
    for i in seq:
        cnt += 1
    return cnt


def result():
    maxLength = 0
    nr = 0
    for i in range(1_000_000):
        length = sequenceLen(collatzSequence(i))
        if length > maxLength:
            maxLength = length
            nr = i
            # print( (i, length))
    return nr


print(result())