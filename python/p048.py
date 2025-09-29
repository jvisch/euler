
def result():
    powers = (i**i for i in range(1, 1000))
    total = sum(powers)
    last_10_chars = str(total)[-10:]
    return last_10_chars


if __name__ == '__main__':
    print(result())
