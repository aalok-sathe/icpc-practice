#! /bin/env/ python3

import modarithmetic

import progress_printer
pp = progress_printer.Progress_printer()

upper_limit = 1000#150221222240

# Infinite generator function
def counter(start):
    while True:
        yield start
        start += 1
# Generator object using gen. function
numbers = counter(2)


# DP array
#numWays = [0,0,1,1,1,2,2,3]
##########  0,1,2,3,4,5,6,7
numWays = [0,0]
nums = [0,1]

def calcNumPrimeReprs(x):
    #print("\nCalculating for %d" % x)
    numWays.append(0)#int(modarithmetic.isPrime(x, 128)))
    nums.append(x)
    #print(nums, "\t", numWays)
    for i in range(2,x//2+1):
        if modarithmetic.isPrime(i,100):
            #print(i,x-i,numWays[i] , numWays[x-i])
            numWays[-1] += int((numWays[i] * numWays[x-i]))
    #print(nums[:])
    #print(numWays[:])

#pp.print_progress(numWays[-1], upper_limit)
for num in numbers:
    calcNumPrimeReprs(num)
    #pp.print_progress(numWays[-1], upper_limit)
    #print(num, numWays[-1], "\n")
    #if numWays[-1] % 10 in {0,}:
    #    print ("\t", num, numWays[-1])
    if numWays[-1] >= upper_limit or num > 11:
        print(list(zip(nums,numWays)))
        print(num)
        break
        
