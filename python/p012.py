import math
import itertools
import p005

def triangleNumbers() :
	n = 2
	nextNumber = 1
	while True:
		yield nextNumber
		nextNumber+=n
		n+=1
		
		
# http://www.wiskundeforum.nl/viewtopic.php?f=28&t=9196#p57485
def divisorsCount(n):
	total = 1
	for f in pm005.factorsCount(n):
		total = total * (f[1]+1)
	return total
	
def result(count=20):
	numbers = triangleNumbers()
	nr = next(numbers)
	while(divisorsCount(nr) < count):
		nr = next(numbers)
	return nr