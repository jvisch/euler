import p003


def result(max=10001):
    primes = p003.primes()
    for _ in range(0, max):
        p = next(primes)
    return p


if __name__ == '__main__':
	print(result())