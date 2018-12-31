m = 100
terms = set([a**b for a in range(2,m+1) for b in range(2, m+1)])

print(len(terms))
