
def patternedMessage(s, p):
	s1=''
	j=0
	for i in p:
		if i =='*':
			if s[j]==' ':
				j+=1
			s1+=s[j]
			j+=1
			if j>=len(s):
				j=0
		else:
			s1+=i
	return s1

print(patternedMessage(input(), input()))