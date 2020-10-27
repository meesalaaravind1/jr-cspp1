def readSet():
	a = set()
	s = input().split()
	for i in s:
		a.add(int(i))
	return a

def minMax(s):
	# your code goes here
	if len(s)==1:
		mini=0
		maxi=0
		for i in s:
			mini=i
			maxi=i
	else:
		mini=9223372036854775807
		maxi=-9223372036854775808
		for i in s:
			if i<mini:
				mini=i
			if i>maxi:
				maxi=i
	return (mini,maxi)

print(minMax(readSet()))


