## very, very, very, very slow

def to_digits(value):
    digits = []
    while value > 0:
        digits.append(value % 10)
        value //= 10
    return reversed(digits)

def from_digits(digits):
    value = 0
    for d in digits:
        value = (value * 10) + d
    return value

def unique_values(items):
    for i in range(len(items) - 1):
        if items[i] in items[i+1:]:
            return False
    return True

def is_pandigital(value):
    if len(value) != 9:
        return False
    if 0 in value:
        return False
    return unique_values(value)


def result():
    value = 10000
    value = 987654321

    value //= 3

    while value > 0:
        if(value % 1000000 == 0):
            print(value)
        first = list(to_digits(1 * value)) 
        second = list(to_digits(2 * value)) 
        digits = first + second
        # 0 may not occur
        if not 0 in digits:
            # all digits must be unique
            if unique_values(digits):
                b = 3
                while(len(digits) < 9):
                    p = b * value
                    digits += list(to_digits(p))
                    b += 1
                # check if it's pandigital
                if is_pandigital(digits):
                    return value, digits
        value -= 1



if __name__ == '__main__':
    value, digits = result()                
    print(f"{value} : {digits}")
    print(from_digits(digits))