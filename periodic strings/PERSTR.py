#! /bin/env/ python3
# Aalok Sathe
import sys

def divides(k, n):
	return (n % k == 0)

def is_periodic(string, k):
	prev = string[:k]
	#print (k,prev)
	for i in range(k,len(string),k):
		cur = string[i:i+k]
		if (prev == str(cur[1:] + cur[0])):
			prev = cur
		else:
			return False
	return True

for string in sys.stdin:
	string = string[:len(string)-1]	# remove "\n"
	for k in range(1,len(string)+1):
		if divides(k, len(string)):
			if is_periodic(string,k):
				print (k)
				break
			#print (string, k, "is_perstr?", is_periodic(string,k))
########
# Alternate solution:
# min_period: start with 1, check next
