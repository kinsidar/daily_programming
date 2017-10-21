def is_prime(p):
    p = abs(p)
    if p < 2:
        return False
    if p == 2:
        return True

    if not p & 1:
    	return False
	 #range starts with 3 and only needs to go up the squareroot of n for all odd numbers
    #for x in range(2, int(sqrt(p)) + 1):
    for x in range(3, int(p**0.5)+1, 2):
        if p % x == 0:
            return False
    return True
    
n = int(input("input a number."))

if is_prime(n):
	print(n, " is prime.")
else:
	i = n - 1
	j = n + 1
	while not is_prime(i):
		i -= 1
	while not is_prime(j):
		j += 1
	print(i , "<" , n , "<" , j)
    