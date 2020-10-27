def readSet():
	a = set()
	s = input().split()
	for i in s:
		a.add(int(i))
	return a

def readList():
	a = []
	s = input().split()
	for i in s:
		a.append(int(i))
	return a

def noIdea(L, A, B):
	# your code goes here
	s=0
	for i in L:
		if i in A:
			s+=1
		if i in B:
			s-=1
	return s


print(noIdea(readList(), readSet(), readSet()))


