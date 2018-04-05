# Aalok Sathe
#! /bin/env/ python3

import sys

line_count = 0
for line in sys.stdin:
    line_count += 1
    
    if line_count == 1:
        continue
    
    initial_num = line.split()[0]    
    line = line.split()[1:]
    
    num_array = [int(x) for x in line]
    
    num_steps = 0
    l = []
    for i in range(len(num_array)):
        l.append(num_array[i])
        num_steps += l.index(num_array[i]) - sorted(l).index(num_array[i])
        l.sort()
        
    print (initial_num, num_steps)
