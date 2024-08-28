def integer_from_string( input_string ) :
	digits = {
		'0':0,
		'1':1,
		'2':2,
		'3':3,
		'4':4,
		'5':5,
		'6':6,
		'7':7,
		'8':8,
		'9':9
	}
	    
	start = 0
	import re
	pattern = r'^[+-]|\d'
	match = re.match(pattern, input_string)
	print('im match', match)
	if match is None:
		return 0
	# print(ord)
	# while start <= len(input_string) or input_string[start] == "":
	# 	start = 1

	sign = 0
	if input_string[start] == '-':
		sign = -1
	
	answer = ''
	for c in input_string[start:]:
		d = digits.get(c,None)
		print('imd ',d)
		if d is None: break
		
		if sign == -1 and ((answer > 214748364) and (answer == 214748364 and d == 9)):
			return -2147483648
		elif sign == 1 and ((answer > 214748364) and (answer == 214748364 and d > 7)):
			return 2147483647
		print('imdad ',answer, d)

		answer = str(answer) + str(d)
	print(answer)
	return int(answer)

# ist = '123'
ist = 'the out not 1000'

ans = integer_from_string(ist)

print('final', ans)

def integer_from_string(input_string):
    # Define constants for the 32-bit integer range
    INT_MIN = -2147483648
    INT_MAX = 2147483647
    
    # Edge case for empty input
    if not input_string:
        return 0

    # Initialize variables
    start = 0
    sign = 1
    result = 0
    
    # Check for leading sign
    if input_string[start] == '-':
        sign = -1
        start += 1
    elif input_string[start] == '+':
        start += 1

    # Iterate over the string and build the number
    for c in input_string[start:]:
        if c.isdigit():
            digit = int(c)
            
            # Check for overflow
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
        else:
            break

    return sign * result

# Example usage:
print(integer_from_string("42"))           # Output: 42
print(integer_from_string("-42"))          # Output: -42
print(integer_from_string("2147483648"))   # Output: 2147483647 (overflow)
print(integer_from_string("-2147483649"))  # Output: -2147483648 (underflow)
print(integer_from_string("abc123"))       # Output: 0 (non-digit characters)
