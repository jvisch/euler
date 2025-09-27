from lib.numbers import to_digits

p = 5
m = (p+1)*(9**p)

terms = []

for n in range(2, m):
    power_of_digits = sum([i**p for i in to_digits(n)])
    if n == power_of_digits:
        terms.append(n)

print(terms)
print("Total: ", sum(terms))
