# Triangle 	  	Tn=n(n+1)/2 	1, 3, 6, 10, 15, ...
# Pentagonal 	Pn=n(3n−1)/2    1, 5, 12, 22, 35, ...
# Hexagonal 	Hn=n(2n−1) 	  	1, 6, 15, 28, 45, ...


import time


def triangle(value):
    return (value * (value + 1)) // 2


def pentagonal(value):
    return (value * (3*value - 1)) // 2


def hexagonal(value):
    return value * (2*value - 1)


start = time.time()

triangles = set()
pentagonals = set()
hexagonals = set()

n = 1

while True:
    t = triangle(n)
    p = pentagonal(n)
    h = hexagonal(n)

    triangles.add(t)
    pentagonals.add(p)
    hexagonals.add(h)

    if t > 40755:  # from description of the problem
        if t in pentagonals and t in hexagonals:
            print(t)
            break
    n += 1

print('done')
print(time.time() - start)
