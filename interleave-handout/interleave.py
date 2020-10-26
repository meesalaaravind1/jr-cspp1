
def interleave(s1, s2):
	i=0
	j=0
	l=min(len(s1),len(s2))
	s=''
	while (i<l and j<l):
		s+=s1[i]+s2[j]
		i+=1
		j+=1
	while (i<len(s1)):
		s+=s1[i]
		i+=1
	while (j<len(s2)):
		s+=s2[j]
		j+=1
	return s

print(interleave(input(), input()))