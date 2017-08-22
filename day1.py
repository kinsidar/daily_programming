# r/dailyprogrammer [17-08-21] Challenge #328 [easy] Latin Squares
import sys

def is_latin_square(n, a):
	if (len(a) != (n*n)):
		return False
	s = set(range(1, n+1))
	for i in range(n):
		row = set(a[i * n + j] for j in range(n))
		col = set(a[j * n + i] for j in range(n))
		if row != s or col != s:
			return False
	return True

#check if latin square
arr_length = int(input("input array length"))
arr = input("input array")
a = list(map(int, arr.split()))

print(is_latin_square(arr_length, a))


