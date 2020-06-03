def factorial(value):
    if value <= 1:
        return 1
    return value * factorial(value-1)


def digits(value):
    while value > 0:
        yield value % 10
        value = int(value / 10)


# def curious_numbers():
#     upper_limit = 7*factorial(9)  # max 7 digits
#     for number in range(3, upper_limit):
#         digit_factorials = (factorial(d) for d in digits(number))
#         if sum(digit_factorials) == number:
#             yield number


def curious_numbers():
    factorials = [1,1] + [factorial(f) for f in range(2,10)] # caching factorials
    upper_limit = 7*factorials[9]  # max 7 digits
    for number in range(3, upper_limit):s
        digit_factorials = (factorials[d] for d in digits(number))
        if sum(digit_factorials) == number:
            yield number


if __name__ == "__main__":
    total = 0
    for n in curious_numbers():
        print(n)
        total = total + n

    print("Answer: {}".format(total))
