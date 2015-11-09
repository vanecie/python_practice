#!/usr/bin/env python

# 1) Return the golden ratio https://en.wikipedia.org/wiki/Golden_ratio as a float
#    Hint: you need to use an import
def solution1():

# 2) Write a function which tests if a list is a palindrome. This means that the list reads the
#    same way forwards as it does backwards i.e. [a,b,c,d,c,b,a]
#    Return True if it is a palindrome, and False if it is not
def solution1(list):

# 3) Compress a list 'A' containing consecutive entries using a run length encoding strategy.
#    You should return a list containing other lists which are the number of repetitions
#    followed by the repeated entry itself. You should not modify the list if the entry
#    is not repeated.
#    https://en.wikipedia.org/wiki/Run-length_encoding
#    For example, the list [1,3,3,3,4,4,4,4,1,5,5,5,5,5,1] should be transformed to
#                          [1,[3,3],[4,4],1,[5,5],1] and the list
#                          ['a','a','a','b','c','c','d','e','f'] should be transformed to
#                          [[3,'a'],'b',[2,'c'],'d','e','f']
def solution3(A):

# 4) Use the RLE data you created above and decompress it back to the original input.
#    Return as the original list.
#    [1,[3,3],[4,4],1,[5,5],1] -> [1,3,3,3,4,4,4,4,1,5,5,5,5,5,1]
#    [[3,'a'],'b',[2,'c'],'d','e','f'] -> ['a','a','a','b','c','c','d','e','f']
#    Hint: You can use isinstance(entry, list) to check if something is an array
def solution4(RLE):

# 5) Sort an array of integers in descending numerical order. Return a sorted array.
#    [5, 6, 3, 7, 8, 2, 0, 1, 9, 4] -> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#    [1, 9] -> [9, 1]
#    Hint: Selection sort or bubble sort is an easy way to solve this problem
def solution5(A):

# 6) FizzBuzz problem. Given a start value S and an end value E, return an array
#    containing the values between S and E (inclusive). Replace any integer that
#    is a multiple of 3 with the string "Fizz", and multiple of 5 with the string
#    "Buzz", and any multiple of 3 and 5 with the string "FizzBuzz".
#    For example, given (5, 15), the returned array would be:
#       ["Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
def solution6(S, E):

# IGNORE EVERYTHING BELOW THIS LINE

def solution1_harness():
	ret = solution1()
	assert str(ret)[:10] == "1.61803398"
	return ret
def solution2_harness():
	ret = solution2([1, 2, 3, 2, 1])
	assert ret == True
	ret = solution2([1, 2, 3, 4, 5])
	assert ret == False
	ret = solution2(['a', 'b', 'b', 'a'])
	assert ret == True
	ret = solution2(['x', 'y', 'z', 'a'])
	assert ret == False
def solution3_harness():
	ret = solution3([1,3,3,3,4,4,4,4,1,5,5,5,5,5,1])
	assert ret == [1,[3,3],[4,4],1,[5,5],1]
	ret = solution3(['a','a','a','b','c','c','d','e','f'])
	assert ret == [[3,'a'],'b',[2,'c'],'d','e','f']
def solution4_harness():
	ret = solution4([1,[3,3],[4,4],1,[5,5],1])
	assert ret == [1,3,3,3,4,4,4,4,1,5,5,5,5,5,1]
	ret = solution4([[3,'a'],'b',[2,'c'],'d','e','f'])
	assert ret == ['a','a','a','b','c','c','d','e','f']
def solution5_harness():
	ret = solution5([5, 6, 3, 7, 8, 2, 0, 1, 9, 4])
	assert ret == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
	ret = solution5([1, 9])
	assert ret == [9, 1]
def solution6_harness():
	ret = solution6(5, 15)
	assert ret == ["Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
	return ret

import sys
import inspect
import traceback

def menu():
	if sys.version_info <= (2, 7):
		solution = raw_input("which solution do you want to run? (1 to 9) (q to quit) ")
	else:
		solution = input("which solution do you want to run? (1 to 9) (q to quit) ")
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
