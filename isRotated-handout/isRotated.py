def rotateRight(s):
	return s[1:len(s)+1]+s[0]

def isRotated(w1, w2):
	for i in range(len(w1)):
		if (w1[i:]+w1[:i] == w2) or (w2[i:]+w2[:i] == w1):
			return True
	if w1[::-1]==w2:
		return True
	return False



print(isRotated(input(), input()))
