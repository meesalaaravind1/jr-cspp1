
def isPerfect(n):
	c=0
	for i in range(1,n):
		if n%i==0:
			c+=i
	return c==n


def nthPerfectNumber(x):
	c=1
	n=6
	while c<=x:
		if isPerfect(n):
			c+=1
		n+=1
	return n-1

print(nthPerfectNumber(int(input())))
# print (isPerfect(int(input())))
