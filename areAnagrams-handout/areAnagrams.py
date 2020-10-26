def areAnagrams(s1, s2):
	s1=s1.lower()
	s2=s2.lower()
	for i in s1:
		if s1.count(i) != s2.count(i):
			return False
	for i in s2:
		if s2.count(i) != s1.count(i):
			return False
	return True



print(areAnagrams(input(), input()))
