def primes(max) :
	# Sieve of Eratosthenes
	# http://en.wikipedia.org/wiki/Eratosthenes#Prime_numbers
	list = [True]*(max-1)
	for b in range(2, len(list)+2):
		if list[b-2] :
			for i in range(b+b, len(list)+2, b):
				list[i-2] = False
	for p in range(2, len(list)+2):
		if list[p-2] :
			yield p
	
def result(max=2*10**6): 
	return sum(primes(max))
	
def primes2(max) :
	# Sieve of Eratosthenes
	# http://en.wikipedia.org/wiki/Eratosthenes#Prime_numbers
	list = [True]*(max-1)
	for b in range(2, len(list)+2):
		if list[b-2] :
			yield b
			for i in range(b+b, len(list)+2, b):
				list[i-2] = False
