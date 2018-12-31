
sumDividers = [ (i, sum([d for d in range(1, i) if i%d is 0])) for i in range(1,10000)]
amicableSets = [ i for i in sumDividers if i[0] != i[1] and (i[1], i[0]) in sumDividers]
total = sum(i[0] for i in amicableSets)

print(total)
