def encodeOffset(s, n):
	if n>0:
		n=n%26
	else:
		n=(abs(n)%26)*-1
	enc=""
	small="abcdefghijklmnopqrstuvwxyz"
	caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in s:
		if i in small:
			pos=small.find(i)
			new=pos+n
			enc=enc+small[new]
		elif i in caps:
			pos=caps.find(i)
			new=pos+n
			enc=enc+caps[new]
		else:
			enc+=i
	return enc

print(encodeOffset(input(), int(input())))
