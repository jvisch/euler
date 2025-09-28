total = 0

for number in range(0, 10**6):
    number_decimal = str(number)
    # is decimal palindrome?
    if number_decimal == number_decimal[::-1]:
        # is binary a palindrome?
        number_binary = f'{number:b}'
        if number_binary == number_binary[::-1]:
            total += number

print(total)
