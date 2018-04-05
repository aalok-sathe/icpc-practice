#! /bin/env/ python3

import sys

def normalize_pair(a, b):
	if a > b:
		return (b, a)
	return (a, b)
	
def to_integer(t):
	for i in range(len(t)):
		t[i] = int(t[i])
	return t

input_dump = []
for string in sys.stdin:
	input_dump.append(string[:len(string)-1])

line_index = 0
while line_index < len(input_dump):

	if len(input_dump[line_index]) < 2:
		break
	
	print(input_dump[line_index])
	
	n, m, s, t = to_integer(input_dump[line_index].split())
	
	graph = {}	# of the form <v> : {x1, x2, x3, ...}: set of graph
	
	incoming = [0 for i in range(n)]
	squawk_value = [0 for i in range(n)]
	
	squawk_value[s] = 1		# this node is infected by the virus.
	current_infected = {s}
	
	# read in the adjacencies
	for i in range(m):	
		line_index += 1
		
		v1, v2 = to_integer(input_dump[line_index].split())
		(v1, v2) = normalize_pair(v1, v2)
		
		graph[v1] = graph.get(v1, set()).union({v2})
		graph[v2] = graph.get(v2, set()).union({v1})
		

	total_count = 1
	
	for time in range(t):
		
		new_infected = set()
		
		for node in current_infected:
			
			# mark neighbors infected, update their number of squawks
			new_infected.update(graph[node])
						
			for neighbor in graph[node]:
				incoming[neighbor] += squawk_value[node]
				total_count += squawk_value[node]
			
			squawk_value[node] = 0
			
		for node in new_infected:
			squawk_value[node] = incoming[node]
			incoming[node] = 0
			
		current_infected = set().union(new_infected)
		
	print(total_count)
	
	line_index += 1
