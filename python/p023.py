max = 10000
max = 28123

def sumDividers(getal):
    total = 0
    for g in range(1, getal):
        if getal % g == 0:
            total += g
    return total

abundant = [ getal < sumDividers(getal) for getal in range(1, max)]
print("Abundant ", len(abundant))

def isAbundant(getal):
    return abundant[getal-1]


def checkNumber(getal):
    for g in range(1, getal // 2 + 1):
        if isAbundant(g) and isAbundant(getal - g):
            return False
    return True


numbers = [getal for getal in range(1, max) if checkNumber(getal) ]
result = sum(numbers)

print( result )
