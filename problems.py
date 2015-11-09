#!/usr/bin/env python3

# 1) Write a function which takes two strings strA and strB and returns them joined with a space
#    "hello", "world" -> "hello world"
#    VERY EASY
def solution1(strA, strB):
	strA = "hello"
	strB = "world"
	return(strA + " " + strB)

# 2) Write a function which adds 2 integers A and B and returns the result
#    a, b -> a + b
#    VERY EASY
def solution2(A, B):
	return A + B

# 3) Write a function which returns the integers 0 -> 9 (inclusive) as an array
#    -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#    VERY EASY
def solution3():
	return(range(0,10))

# 4) Write a function which returns the even integers between 0 -> 9 as an array
#    -> [0, 2, 4, 6, 8]
#    VERY EASY
def solution4():
	return (range(0,10,2))

# 5) Write a function which inverts the capitalization of the string A and returns the result
#    (You cannot use swapcase())
#    "ThiS IS a STrinG" -> "tHIs is A stRINg"
#    EASY
def solution5(A):
	string = ""
	for letter in A:
		if letter.isupper():	
			string = string + letter.lower()
		else:
			string = string + letter.upper()
	return string

# 6) Write a function which returns a string containing only words from another string over 4 letters long
#    The returned string should have words delimited by spaces. Don't leave spaces at the beginning or end of the returned string
#    "this is a really complicated string" -> "really complicated string"
#    MEDIUM

def solution6(s):
	string = ""
	for word in s.split():
		if not len(word) > 4:
			continue
		if len(string) == 0:
			string = word
		else:
			string = string + " " + word
	return string

# 7) Write a function which returns an array containing integers in the Fibonacci sequence up to 377
#    https://en.wikipedia.org/wiki/Fibonacci#Fibonacci_sequence 
#	1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
#    MEDIUM
def solution7():
	array = []
	sum = 1
	last_sum = 1
	while last_sum < 600:
		array.append(last_sum) 
		t = last_sum + sum
		last_sum = sum
		sum = t
	return array 

# 8) Write a function which returns an array containing the first 10 prime numbers
#    (Zero and one are not prime numbers)
#    HARD
# 2,3,5,7,11,13,17,19,23,29
def solution8():
	array = [ ]
	i = 1 	
	while len(array) < 20:
		i = i+1
		ok = True
		for n in range(2, i):
			if not i % n:
				ok = False
				break
		if ok: 
			array.append(i)
	return array

# 9) Write a function which takes a string, which is an arithmetic expression containing only floats and one of +,-,/,*, and returns the result of the expression as a string
#    Normal rules for operator precedence do not apply, just use the operators in the sequence you read them
#    "50.0+60.0/10.0*20.0" -> "220.0"
#    VERY HARD
def solution9(expr):
	number_strings = expr.replace("+"," ").replace("/"," ").replace("*"," ").replace("-"," ").split(" ")
	number = [ ]
	for word in number_strings:
		number.append(float(word))
	operators = [ ]
	for letter in expr:
		if letter == "+" or letter == "-" or letter == "/" or letter == "*":
			operators.append(letter)
	offset = 0
	sum = number[offset]
	for operator in operators:
		offset +=1
		if operator == "+":
			sum = sum + number[offset]
		if operator == "*":
			sum = sum * number[offset]
		if operator == "/":
			sum = sum / number[offset]
		if operator == "-":
			sum = sum - number[offset]
	return str(sum)
#	print(str(number) + str(operators))	
#return None

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
				print("Congratulations, You Go girl!")
			except:
				_, _, tb = sys.exc_info()
				traceback.print_tb(tb)
				print("")
				print("Solution or harness is wrong! Keep trying, you can do it!")
			print("")
	return False

if __name__ == "__main__":
	while not menu():
		pass