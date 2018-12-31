def get_digits(value):
    digits = list()
    while value > 0:
        digits.append(value % 10)
        value //= 10
    digits.reverse()
    return digits

p = 5
m = (p+1)*(9**p)

terms = []

for n in range(2, m):
    power_of_digits = sum([i**p for i in get_digits(n)])
    if n == power_of_digits:
        terms.append(n)

print(terms)
print("Total: ", sum(terms))