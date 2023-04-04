
def divide(a, b):
    remainders = []
    result = a // b
    fraction =  str(result)
    remainder = a - (result * b)
    fraction += "."
    while remainder > 0 and remainder not in remainders:
        remainders.append(remainder)
        remainder *= 10
        result = remainder // b
        remainder -= (result * b)
        fraction += str(result)
    idx = -1
    if remainder in remainders:
        idx = remainders.index(remainder)
    return a, b, fraction, remainders, idx, len(remainders)

fractions = [divide(1,i) for i in range(1, 1000) ]

longest = max(fractions, key=lambda item: item[-1]-item[-2])
print(longest)

# for f in fractions:
#     print(f)

# for i in range(1,30) :
#     print(1, " / ", i)
#     print(1/i)
#     print( divide(1,i))
#     print()