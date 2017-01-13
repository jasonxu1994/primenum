#!/usr/bin/env python3

def primenum(n):
	X = True
	list = [2, 3, 5, 7]
	import math
	s = math.floor(math.sqrt(n))
	if s % 2 == 0:
		s -= 1
	if n not in list and s > list[-1]:
		for i in list:
			if n % i == 0:
				X = False
				break
		if X:
			while s > list[-1]:
				if n % s == 0:
					X = False
					break
				s -= 2
	return X
N = int(input("Input:"))
if primenum(N):
	print("Yes")
else:
	print("No")
