'''#Problem #1: Run Length Encoding --> #1 decompress: return array as [1,3,3,3,4,4,4,4,1,5,5,5,5,5,1] 
array = [1,[3,3],[4,4],1,[5,5],1]

new = [ ]
for i in array:
	if isinstance(i,list):
		n= i[0]
		v= i[1]
		for j in range(n):
			new.append(v)	
	else:
		new.append(i)
print (new)'''
		


#Problem #2: Palindromes--> return True if a palindrome

old = [1,2,3,4,5,4,3,2,1]

for i in range(len(old)-1,-1,-1):
	j = len(old) - 1 - i
	if old[i] != old[j]:
		print (False)

print(True)
