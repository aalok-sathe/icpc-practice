# In the first part of this 2 part lab, you will write a python program to do
# some Modular Arithmetic basics. Pseudocode for all of these is in your book.

# Basics of Python Programming were covered in the first few minutes of lab.
# See the Python Example File for examples of functions.

from random import randint
import math
import random


# function powersOfTwo
# inputs: integer e (that is to be used as an exponent elsewhere)
# outputs: list of exponenets of two that sum to the exponent e
# i.e., 2^(a1+a2+...+an) = 2^(e)
#def powersOfTwo(e, s=set()):
#	#print("s",s)
#	if e == 0:
#	    #print(s)
#	    l = list(s)
#	    s -= s
#	    return l
#	s.add(int(math.log(e,2)//1))
#	return powersOfTwo(e-2**(math.log(e,2)//1), s)
#print(powersOfTwo(222))
#print(powersOfTwo(47))

# function extGCD
# inputs: two integers x,y
# outputs: three integers: d,s,t such that
#   d = gcd(x,y)
#   sx + ty = d
def extGCD(x, y):
            
    r = [y, x]
    s = [1, 0]
    t = [0, 1]
    
    while (x and y):
        r.append(y % x)
        s.append(s[-2] - y//x * s[-1])
        t.append(t[-2] - y//x * t[-1])
        y,x = x, y%x
        
    #print(x,y,r,s,t)
    return (y,s[-2],t[-2])
    
#print(extGCD(105, 63))
#print(extGCD(63, 105))

# function expMod
# inputs: three integers b,e,n with e >= 0
# output: b^e mod n
# This algorithm must work using the *fast* exponention algorithm described in
# lecture. The slow exponentiation algorithm is in the example file.
def expMod(b,e,n):
    b %= n # If b is greater, take mod before starting
    expmod = 1
    
    while e:
        if e % 2 == 1:
            expmod = (expmod * b) % n
        e >>= 1
        b = (b * b) % n
    
    return expmod

    # Get a list of the exponents of two making up the exponent e
    #expList = list(powersOfTwo(e))
    #twosPowerMods = {0:b%n, 1:(b**2)%n}
        
    # Populate a dictionary with mods of the base raised to powers of two
    #for i in range(2,max(expList)+1):
    #	twosPowerMods[i] = (twosPowerMods[i-1])**2 % n
    
    # Set the first element and then DP over the list using successive mods
    #expList[0] = twosPowerMods.get(expList[0])
    #for i in range(1,len(expList)):
    #    expList[i] = (expList[i-1] * twosPowerMods[expList[i]]) % n # DP step
    
    #return expList[len(expList)-1]
    
#print(expMod(random.getrandbits(333),random.getrandbits(333),random.getrandbits(333)))

# function expModSlow
# inputs: three integers b,e,n with e >= 0
# output: b^e mod n
# This will work, but will take a long time for large e.
# This may be useful for debugging
def expModSlow(b,e,n):
    x = 1
    for i in range(e):
        x *= b
        x %= n
    return x


# function isprime(p,k)
# input: a positive integer p and a positive integer k
# output: true if p is (probably) prime, false otherwise you use use fermat's
# test on p for k iterations. the probability that we return true for a
# number that isn't actually prime is at most (1/2)^k, unless n is a
# carmichael number, which is also very unlikely.
def isPrime(p,k):
    for a in range(2,min(k+2, p-1)):
    	if expMod(a,p-1,p) != 1:
    		return False
    return True
