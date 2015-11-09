# 6) FizzBuzz problem. Given a start value S and an end value E, return an array
#    containing the values between S and E (inclusive). Replace any integer that
#    is a multiple of 3 with the string "Fizz", and multiple of 5 with the string
#    "Buzz", and any multiple of 3 and 5 with the string "FizzBuzz".
#    For example, given (5, 15), the returned array would be:
#       ["Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]

array = [ ]
S = 0
E = 56
for s in range(S, E+1):
	if not s % 15:
		array.append(str("FizzBuzz"))
	elif not s % 3:
		array.append(str("Fizz"))
	elif not s % 5:
		array.append(str("Buzz"))
	else:
		array.append(s)
print(array)

		
	