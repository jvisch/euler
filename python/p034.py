from lib.numbers import to_digits, factorial


def curious_numbers():
    factorials = [1, 1] + [factorial(f)
                           for f in range(2, 10)]  # caching factorials
    upper_limit = 7*factorials[9]  # max 7 digits
    for number in range(3, upper_limit):
        digit_factorials = (factorials[d] for d in to_digits(number))
        if sum(digit_factorials) == number:
            yield number


if __name__ == "__main__":
    total = 0
    for n in curious_numbers():
        print(n)
        total = total + n

    print("Answer: {}".format(total))
