#! /bin/env/ python3
# Aalok S., Hammad H., Paul T. // 3.2018
import sys

lines = []

for line in sys.stdin:
    lines.append(line[:-1])
    if line[:-1] == '0':
        break
        
indexTracker = 0

#while(numLines != '0' and flag):
try:
    while(lines[indexTracker] != '0'):

        numLines = int(lines[indexTracker])
        
        currentColumn = 0
        
        # Specific test case
        for i in range(int(numLines)):
        
            indexTracker += 1
            
            line = lines[indexTracker][currentColumn:]
            
            if (len(line) == 0) or (line[0] in {'',' '}):
                pass
            else:
                word = line.split()[0]
                currentColumn += len(word)
                
        indexTracker +=1
        
        print(currentColumn+1)
        
except Exception:
    pass
