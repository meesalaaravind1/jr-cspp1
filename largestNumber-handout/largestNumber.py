
def largestNumber(s):
	n1=''
	n2=''
	flag=True
	for i in s:
		if ord(i)>47 and ord(i)<58:
			n1+=i
		elif n2=='':
			n2=n1
			n1=''
		elif n1!='' and n2!='':
			if int(n1)>int(n2):
				n2=n1
				n1=''
	if n2!='':
		return int(n2)
	else:
		return 0
print(largestNumber(input()))
print(largestNumber("fkahfahf kjfh ;lfh 98y4h 4p3b "))

