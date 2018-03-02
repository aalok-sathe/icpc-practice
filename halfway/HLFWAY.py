#! /bin/env/ python3
# Aalok Sathe

import sys

for line in sys.stdin:
	print ((lambda n: (int(.25*(-(2-4*n)-((2-4*n)**2-8*n*(n-1))**.5))+1))(int(line.split()[0])))
