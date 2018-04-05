#! /bin/env/ python3

import modarithmetic # for .isPrime 

target = 1000 #int(input("Target?\t"))

# Similar to coins problem
denominations = []

# Populate primes as ``denominations"
last_index = None
num_ways = {0:{}, -1:{}}
for num in range(2,target+1):
    if modarithmetic.isPrime(num,100):
        denominations.append(num)
        num_ways[0][num] = 1
        num_ways[-1][num] = 0
        last_index = num

# DP Step
for i in range(1,1+target):
    num_ways[i] = dict(num_ways[-1])
    for d in range(0,len(denominations)):
        if denominations[d] > i:
            pass#continue
        num_ways[i][denominations[d]] = num_ways.get(i-denominations[d],{}).get(denominations[d],0) + num_ways[i][denominations[d-1]]
        #num_ways[i]["T"] += num_ways[i][denominations[d]]

# See for which number the answer matches
for i in range(len(num_ways)):
    if num_ways[i][last_index] >= 150221222240:
        print(i)
        break

