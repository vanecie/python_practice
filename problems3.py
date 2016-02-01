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
	games = [ ]
	for i in range(1,len(list)):
		P1_wins = 0
		P2_wins = 0 
		for e in list[i]:
			if e[0] == e[1]:
				continue
			if e[0] == "S" and e[1] == "P":
				P1_wins = P1_wins + 1
			elif e[0] == "P" and e[1] == "R":
				P1_wins = P1_wins + 1
			elif e[0] == "R" and e[1] == "S":
				P1_wins = P1_wins + 1
			else: 
				P2_wins = P2_wins + 1
		if P1_wins > P2_wins:
			games.append(1)
		else:
			games.append(2)
	return games
			



# Print hex str
# Print a string in hexadecimal
#
# input: "A0!"
# output: "413021"
#
# input: "Hi, People"
# output: "48692C2050656F706C65"

def solution3(string):
	lady = ""
	for sexy in string:
		x = ord(sexy) % 16
		if x>=0 and x<=9:
			x = str(x)
		if x>=10 and x<=15:
			x = chr(x+55)
		lady = lady + str(ord(sexy)/16) + x
	return lady

# emirp prime
#
# Given a list of input integers, find a value greater
# than or equal to that integer which is prime when
# read as a string in both directions.
#
# For example, 13 and 31 are both prime numbers, so
# if the input value given was '12', '13' would be
# the proper output.
#
# The list passed into the function contains the
# number of numbers to test, followed by the numbers
# themselves.
#
# Input:
#  3
#  10
#  20
#  50
#
# Output:
#  11
#  31
#  71

def is_prime(number):
	prime = True
	for mod in range(2,number):
		if number % mod == 0:
			prime = False
			break
	return prime

def reverse (number):
	number_reversed_str = str(number)[::-1]
	number_reversed = int(number_reversed_str)
	return number_reversed

def solution4(list):
	output = []
	for i in range(1,len(list)):
		number = list[i]
		while True:
			if is_prime(number):
				if is_prime(reverse(number)):
					break
			number = number + 1
		output.append(number)
	return output

# Knight's Tour
#
# 8 | - - - - - - - -
# 7 | - - - - - - - -
# 6 | - - 2 - 1 - - -
# 5 | - 3 - - - 0 - -
# 4 | - - - X - - - -   X - depicts the Knight's initial position here
# 3 | - 4 - - - 7 - -   and digits - landing squares for 8 different jumps
# 2 | - - 5 - 6 - - -
# 1 | - - - - - - - -
#   +-----------------
#     a b c d e f g
#
# Given a board of dimensions NxM, and a removed square P,Q,
# calculate a series of 'rotations' of the Knight such that
# it would traverse every square in the board (except the
# removed square) but only visit each square once.
#
# The answer assumes you will start at 0,0 and test rotations
# in sequence, so for example rotation 0 would be the first
# valid move. The board tested is 3x4 and the removed square
# is at 3,2. The coordinates of the removed square are
# 0-indexed.
#
# The input data is formatted like:
# [ Board_N, Board_M, Removed_P, Removed_Q ]
#
# The output data should be formatted like:
# [ Start_X, Start_Y, Rotation, Rotation, Rotation, ... ]

def solution5(list):
	return list

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

def solution4_harness():
	ret = solution4([ 3, 10, 20, 50 ])
	assert ret == [ 11, 31, 71 ]
	return ret

def solution5_harness():
	ret = solution5([ 3, 4, 3, 2 ])
	assert ret == [ 0, 0, 0, 3, 6, 0, 3, 6, 3, 0, 6, 3 ]
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
