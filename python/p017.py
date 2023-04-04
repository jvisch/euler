numbers = {
	1: 'one',
	2: 'two', 
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine',
	10: 'ten',
	11: 'eleven',
	12: 'twelf',
	13: 'thirteen',
	14: 'fourteen',
	15: 'fifteen',
	16: 'sixteen', 
	17: 'seventeen',
	18: 'eighteen',
	19: 'nineteen',
	20: 'twenty',
	30: 'thirty',
	40: 'fourty',
	50: 'fifty',
	60: 'sixty',
	70: 'seventy',
	80: 'eighty',
	90: 'ninety'
	}

def result():
	total = 0
	for n in range(1, 1001):
		total += countLetters(say(n))
	return total
	
def countLetters(s):
	cnt = 0
	for c in s:
		if c.isalpha():
			cnt += 1
	return cnt
	
def say(n):
	if n <= 1000:
		if n == 0:
			return ''
		elif n in numbers:
			return numbers[n]
		else:
			if n < 100:
				tens = int(n / 10)
				value = say(tens*10)
				rest = n % 10
				if rest > 0:
					value = value + '-' + say(rest)
			elif n < 1000:
				hundreds = int(n/100)
				value = say(hundreds) + ' hundred'
				rest = n % 100
				if rest > 0:
					value = value + ' and ' + say(rest)
			elif n == 1000:
				value = say(1) + ' thousand'
			else:
				raise ValueError
			numbers[n] = value.strip()
			return numbers[n]		
	else:
		raise ValueError()