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
