def result1() :
	factors = range(999, 99, -1) # van 999 t/m 100
	lst = [a*b for a in factors for b in factors if str(a*b) == str(a*b)[::-1]] # [::-1] is inverteren
	return max(lst)
	
def palindromes() :
	f = range(999, 99, -1)
	for a in f:
		for b in f:
			p = a*b
			if str(p) == str(p)[::-1] :
				yield p	
	
def result2():
	return max(palindromes())

if __name__ == '__main__':
	print('result1: ' + str(result1()))
	print('result2: ' + str(result2()))