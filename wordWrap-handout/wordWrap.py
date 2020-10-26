
def wordWrap(s,n):
	s1=''
	j=0
	s=s.strip()
	for i in s:
		if i!=' ':
			s1+=i
		elif i==' ':
			s1+='-'
		j+=1
		if j>=n:
			j=0
			s1+='\n'
	return s1


print(wordWrap(input(), int(input())))
