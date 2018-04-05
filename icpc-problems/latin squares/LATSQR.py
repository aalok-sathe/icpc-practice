#! /bin/env/ python3
# Aalok Sathe

import sys

input_dump = []
for string in sys.stdin:
	input_dump.append(string[:len(string)-1])
	
index = 0
while index < len(input_dump):

	n = int(input_dump[index])
		
	matrix = []
	for lineindex in range(index+1, index+1+n):
		row = []
		for i in range(n):
			row.append(ord(input_dump[lineindex][i]))
		matrix.append(row)
	
	is_latin = True
	for rowindex in range(len(matrix)):
		whichchars = set()
		for colindex in range(len(matrix)):
			if matrix[rowindex][colindex] in whichchars:
				is_latin = False
				break
			else:
				whichchars.add(matrix[rowindex][colindex])
		if not is_latin:
			break
	
	is_reduced = True
	if is_latin:
		for (first, second) in zip(matrix[0][0:], matrix[0][1:]):
			if first > second:
				is_reduced = False
				break
		if is_reduced:
			for i in range(0,len(matrix)-2):
				if matrix[i][0] > matrix[i+1][0]:
					is_reduced = False
					break
		if is_reduced:
			print("Reduced")
		else:
			print("Not Reduced")
	else:
		print("No")
	
	#print(matrix)
		
	index += (n + 1)
