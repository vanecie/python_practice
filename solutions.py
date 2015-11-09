#!/usr/bin/env python3

# 1) Write a function which takes two strings strA and strB and returns them joined with a space
#    "hello", "world" -> "hello world"
#    VERY EASY
def solution1(strA, strB):
	return strA + " " + strB

# 2) Write a function which adds to integers A and B and returns the result
#    a, b -> a + b
#    VERY EASY
def solution2(A, B):
	return A + B

# 3) Write a function which returns the integers 0 -> 9 (inclusive) as an array
#    -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#    VERY EASY
def solution3():
	return list(range(0,10))

# 4) Write a function which returns the even integers between 0 -> 9 as an array
#    -> [0, 2, 4, 6, 8]
#    VERY EASY
def solution4():
	return list(range(0,10,2))

# 5) Write a function which inverts the capitalization of the string A and returns the result
#    (You cannot use swapcase())
#    "ThiS IS a STrinG" -> "tHIs is A stRINg"
#    EASY
def solution5(A):
	B = ""
	for i in range(len(A)):
		if A[i].isupper():
			B += A[i].lower()
		else:
			B += A[i].upper()
	return B

# 6) Write a function which returns a string containing only words from another string over 4 letters long
#    The returned string should have words delimited by spaces
#    "this is a really complicated string" -> "really complicated string"
#    MEDIUM
def solution6(s):
	new_words = None
	for word in s.split():
		if len(word) <= 4:
			continue
		if new_words:
			new_words += " " + word
		else:
			new_words = word
	return new_words

# 7) Write a function which returns an array containing integers in the Fibonacci sequence up to 377
#    https://en.wikipedia.org/wiki/Fibonacci#Fibonacci_sequence
#    MEDIUM
def solution7():
	fibon = [1, 1]
	offset = 0
	while True:
		fibon.append(fibon[offset] + fibon[offset + 1])
		if fibon[-1] >= 377:
			break;
		offset += 1
	return fibon

# 8) Write a function which returns an array containing the first 10 prime numbers
#    (Zero and one are not prime numbers)
#    HARD
def solution8():
	i = 2
	primes = []
	while True:
		prime = True
		for j in range(2, i):
			if not i % j:
				prime = False
				break
		if prime:
			primes.append(i)
		if len(primes) == 20:
			break
		i += 1
	return primes

# 9) Write a function which takes an string, which is arithmetic expression containing only floats and one of +,-,/,*, and returns the result of the expression as a string
#    Normal rules for operator precedence do not apply, just use the operators in the sequence you read them
#    "50.0+60.0/10.0*20.0" -> "220.0"
#    VERY HARD
def solution9(expr):
	number_strs = expr.replace("+", " ").replace("-", " ").replace("*", " ").replace("/", " ").split()
	operators = []
	for c in expr:
		if c == '+' or c == '-' or c == '*' or c == '/':
			operators.append(c)

	numbers = []
	try:
		for number_str in number_strs:
			numbers.append(float(number_str))
	except ValueError:
		print("Expression '" + expr + "' is invalid")
		return ""

	if len(numbers) - 1 != len(operators):
		print("Invalid number of numbers (" + str(len(numbers)) + ") vs number of operators (" + str(len(operators)) + ")")
		return ""

	sum = numbers[0]
	offset = 1
	for operator in operators:
		if operator == "+":
			sum += numbers[offset]
		elif operator == "-":
			sum -= numbers[offset]
		elif operator == "*":
			sum *= numbers[offset]
		elif operator == "/":
			sum /= numbers[offset]
		offset += 1

	return str(sum)

# IGNORE EVERYTHING BELOW THIS LINE

def solution1_harness():
	ret = solution1("hello", "world")
	assert ret == "hello world"
	return ret
def solution2_harness():
	ret = solution2(1, 99)
	assert ret == 100
	return ret
def solution3_harness():
	ret = solution3()
	assert ret == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	return ret
def solution4_harness():
	ret = solution4()
	assert ret == [0, 2, 4, 6, 8]
	return ret
def solution5_harness():
	ret = solution5("ThiS IS a STrinG")
	assert ret == "tHIs is A stRINg"
	return ret
def solution6_harness():
	ret = solution6("this is a really complicated string")
	assert ret == "really complicated string"
	return ret
def solution7_harness():
	ret = solution7()
	assert ret == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
	return ret
def solution8_harness():
	ret = solution8()
	assert ret == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
	return ret
def solution9_harness():
	ret = solution9("50.0+60.0/10.0*20.0")
	assert ret == "220.0"
	return ret

import sys
import inspect
import traceback

def menu():
	solution = raw_input("which solution do you want to run? (1 to 9) (q to quit) ")
	if solution == "q":
		return True
	if solution.isdigit():
		harness_fn = globals()["solution" + str(solution) + "_harness"]
		raw_fn = globals()["solution" + str(solution)]
		print("")
		print(inspect.getsource(raw_fn))
		if harness_fn:
			try:
				ret = harness_fn()
				if ret:
					print(ret)
			except:
				_, _, tb = sys.exc_info()
				traceback.print_tb(tb)
				print("")
				print("Solution or harness is wrong!")
			print("")
	return False

if __name__ == "__main__":
	while not menu():
		pass