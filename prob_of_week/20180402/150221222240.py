#! /bin/env/ python3

import modarithmetic

target = int(input("Target?\t"))

denominations = []
#denominations.reverse()

num_ways = {0:{}, -1:}
for num in range(target+1):
    if modarithmetic.isPrime(num,100):
        denominations.append(num)



for i in range(1,1+target):
    num_ways[i] = {1:1,5:0,25:0,50:0,100:0,500:0,2000:0}
    for d in range(0,len(denominations)):
        if denominations[d] > i:
            pass#continue
        num_ways[i][denominations[d]] = num_ways.get(i-denominations[d],{}).get(denominations[d],0) + num_ways[i][denominations[d-1]]
        #num_ways[i]["T"] += num_ways[i][denominations[d]]

#for i in range(1,len(num_ways)):
print(num_ways[target][2000])
    
    
#
#
#   change[i,j] =  change[i,j-1]
#                + change[i-j,j]
#


'''
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
''' 
