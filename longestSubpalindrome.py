def longestSubpalindrome(str):
	longest = ""
	for i in range(len(str)+1):     	
		for j in range(len(str)+1):
			str1 = str[i:j]
			if(isPal(str1)):
				if(len(str1)>len(longest)):
					longest = str1
				elif(len(str1)==len(longest)):
					if(str1>longest):
						longest = str1

	return longest


def isPal(str):
	return str!="" and str==str[::-1]


print(longestSubpalindrome(input()))

#longestSubpalindrome("ab-4-be!!!")