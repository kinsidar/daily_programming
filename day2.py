from math import sqrt

def is_prime(p):
	if p < 2:
		return False
	if p/2 == 0:
		return False
	if p/3 == 0:
		return False
