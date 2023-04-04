def result(max=100):
    numbers = range(1, max+1)
    sumOfSquares = sum(map(lambda n: n**2, numbers))
    squareOfSum = sum(numbers)**2
    return squareOfSum-sumOfSquares

if __name__ == '__main__':
    print(result())