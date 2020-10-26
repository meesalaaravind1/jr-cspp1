def checkPalin(word):
	'''
	I have given an input as word and it should check whether it is palindrome
	1.Reverse the string
	2.compare word with revresed word
	3.return true or false
	'''
	return word[::-1] == word

def longestSubpalindrome(s):
	'''
		given word s-find the longest palindrome
		concepts used :
		1.string slicing
		2.for loops
		3.conditions

		Conditions to be checked:
		find longest palindrome
		if both has same length find the lexicographical order and return that string.
	'''
	large = ''
	for i in range(len(s)+1):
		for j in range(len(s)+1):
			s1=s[i:j]
			print (s1)
			if checkPalin(s1):
				if len(s1)>len(large):
					large=s1
					print (large,'large')
				elif len(s1)==len(large):
					if s1>large:
						large=s1
						# print (large,'large')
	return large

print(longestSubpalindrome(input()))