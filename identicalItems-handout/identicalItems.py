def readSet():
	a = set()
	s = input().split()
	for i in s:
		a.add(int(i))
	return a

def identicalItems(s1, s2):
	# your code goes here
	s=set()
	for i in s1:
		if i in s2:
			s.add(i)
	return s

print(identicalItems(readSet(), readSet()))


