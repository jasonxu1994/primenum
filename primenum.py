#!/usr/bin/env python3

def primenum(n):
	X = True
	list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 77, 79, 83, 89, 91, 97]
	if n not in list:
		if n < list[-1]:
			X = False
		if n > list[-1]:
			for i in list:
				if n % i == 0:
					X = False
					break
			if X:
				import math
				s = math.floor(math.sqrt(n))
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
