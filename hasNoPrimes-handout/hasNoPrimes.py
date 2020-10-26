def read2DArray():
	a = []
	l = int(input())
	for i in range(l):
		s = input().split(" ")
		t = []
		for j in range(len(s)):
			t.append(int(s[j]))
		a.append(t)
	return a

def isPrime(n) :

    # Corner cases
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6

    return True

def hasNoPrimes(l):
	# your code goes here
	for i in l:
		for j in i:
			if isPrime(j):
				return False
	return True


print(hasNoPrimes(read2DArray()))


