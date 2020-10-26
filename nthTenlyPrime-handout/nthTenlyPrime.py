def isPrime(n):
    # Corner case
    if (n <= 1):
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

def tenSum(n):
	c=0
	while n>0:
		rem=n%10
		c+=rem
		n=n//10
	return c==10

def nthTenlyPrime(n):
	c=-1
	num=2
	while c!=n:
		if isPrime(num) and tenSum(num):
			c+=1
			print(c,num)
		num+=1
	return num-1

print(nthTenlyPrime(int(input())))






