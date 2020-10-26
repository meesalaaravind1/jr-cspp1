def collapseWhitespace(s):
	s1=''
	c=0
	for i in s:
		if i =='\t' or i == '\n' or i==' ':
			c+=1
		elif c>0:
			c=0
			s1+=' '+i
		elif c==0:
			s1+=i

	return s1.strip()
	# s=s.split(' ')
	# s=''.join(s)
	# s=s.split('\n')
	# s=''.join(s)
	# s=s.split('\t')
	# s=''.join(s)
	# s=list(s)
	# s=' '.join(s)
	# return s.strip()


print(collapseWhitespace(input()))
