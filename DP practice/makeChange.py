#! /bin/env/ python3

target = int(input("Target?\t"))

denominations = [1,5,25,50,100,500,2000]
#denominations.reverse()

num_ways = {0: {1:1,5:1,25:1,50:1,100:1,500:1,2000:1,},}

for i in range(1,1+target):
    num_ways[i] = {1:1,5:0,25:0,50:0,100:0,500:0,2000:0}
    for d in range(0,len(denominations)):
        num_ways[i][denominations[d]] = num_ways.get(i-denominations[d],{}).get(denominations[d],0) + num_ways[i][denominations[d-1]]

print(num_ways[target][2000])
    
#
#
#   change[i,j] =  change[i,j-1]
#                + change[i-j,j]
#


