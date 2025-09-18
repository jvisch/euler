from p046 import Primes

x = []

m = 1_000_000

primes = Primes.primes()
p = next(primes)
while sum(x) < m:
    x.append(p)
    p = next(primes)

# print(x)

result = []

for start in range(len(x)):
    for end in range(start + 1, len(x)+1):
        if end - start > len(result):
            y = x[start:end]
            s = sum(y)
            if s < m and Primes.is_prime(sum(y)):
                print(y)
                result = y

print(result)
print(sum(result))
