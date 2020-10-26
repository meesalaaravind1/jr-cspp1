def replace(s1, s2, s3):
	l=s1.split(s2)
	s=''
	for i in range(len(l)-1):
		s+=l[i]+s3
	s+=l[-1]
	return s


print(replace(input(), input(), input()))
