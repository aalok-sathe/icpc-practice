#! /bin/env/ python3

import sys

for line in sys.stdin:
    
    line = line[:-1]
    
    dim = len(line)
    
    matrix = []
    
    current_start = 0
    current_end = 0
    current_max = 0
    
    for start in range(0,dim):
        color = line[start]
        
        difference = 0
        
        for end in range(start,dim):
        
            if color == line[end]:
                difference += 1
            else:
                difference -= 1
            
            if abs(difference) > current_max:
                current_max = abs(difference)
                current_start = start
                current_end = end
    print ("%d %d" % (1+current_start,1+current_end)
