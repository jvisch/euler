def result():
    numbers = [n for n in range(1, 1000) if n % 3 == 0 or n % 5 == 0]
    return sum(numbers)


print(result())
