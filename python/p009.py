import math

def result():
	for a in range(1, 1000) :
		for b in range(1, 1000) :
			c = math.sqrt(a**2 + b**2)
			d = int(c)
			if c == d:
				if a+b+c == 1000:
					return a*b*d

def main():
	print(result())

if __name__ == '__main__':
	main()