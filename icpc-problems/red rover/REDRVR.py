# Aalok Sathe
#! /bin/env/ python3

import sys
import math

for line in sys.stdin:
	
	line = line[:len(line)-1]
	current_min_cost = len(line)
	current_str = ''
	
	for strlen in range(2, len(line) // 2):
		for substr_index in range(len(line) - strlen):
			current_min_cost = min(current_min_cost, len(line) - (strlen-1)*line.count(line[substr_index:substr_index+strlen]) + strlen)
			# debug print
			#print(current_min_cost)
	print(current_min_cost)
