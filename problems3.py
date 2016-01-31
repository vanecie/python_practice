#!/usr/bin/env python3

# 1) Sort the words provided in the list 'list' and return them as an array of sorted words
def solution1(list):
	for i in range(len(list)-1):
		minm = ord(list[i][0])
		new_index  = i 
		for j in range (i+1, len(list)):
			if ord(list[j][0]) < minm:
				minm = ord(list[j][0])
				new_index = j
			if new_index != i:
				t= list[new_index]
				list[new_index] = list[i]
				list[i] = t					
	return list

# Rock Paper Scissors
# Determine which player wins a game of RPS based on a record of the game
#
# Example:
#  Input data:
#   3
#   SS PR
#   PR RS PS PP SP
#   PS RR PS RP
#
#  Correct output:
#   1 1 2

def solution2(list):
	return

# Print hex str
# Print a string in hexadecimal
#
# input: "A0!"
# output: "413021"
#
# input: "Hi, People"
# output: "48692C2050656F706C65"

def solution3(str):
	return

# IGNORE EVERYTHING BELOW THIS LINE

def solution1_harness():
	list = [ "horse", "dog", "snake", "cat" ]
	ret = solution1(list)
	assert ret == [ "cat", "dog", "horse", "snake" ]
	return ret

def solution2_harness():
	list = [ 3, [ "SS", "PR" ], [ "PR", "RS", "PS", "PP", "SP" ], [ "PS", "RR", "PS", "RP" ] ]
	ret = solution2(list)
	assert ret == [ 1, 1, 2 ]
	return ret

def solution3_harness():
	ret = solution3("A0!")
	assert ret == "413021"
	ret = solution3("Hi, People")
	assert ret == "48692C2050656F706C65"
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
					print(str(ret) + " "+ "Nice job...You go girl!") 
			except:
				_, _, tb = sys.exc_info()
				traceback.print_tb(tb)
				print("")
				print("Try again... you got it!!!")
			print("")
	return False

if __name__ == "__main__":
	while not menu():
		pass
