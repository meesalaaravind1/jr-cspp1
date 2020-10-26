def readArray():
    n = int(input())
    l = []
    for i in range(n):
    	l.append(input())
    return l

def isAnagram(s1,s2):
    '''This function is used to check whether two strings are anagram of each other
    1. Have to return false if both strings don't have the same length
    2. Have to iterate through the s1 and return false if the count of each character in s1 not equals to
        count of each character in s2
    3. If you are done with the entire loop then they are anagrams so return True
     '''
    if len(s1)!=len(s2):
        return False
    for i in s1:
        if s1.count(i)!=s2.count(i):
            return False
    return True

def mostAnagrams(l):
    '''
    input : list of strings
    output : the string which has most number of anagrams in the list
    Conditions to be checked:
    1.find the max count of anagrams.
    2.if the count of anagrams are equal then, you have to follow the alphabetical order and give the first
        string as output

    Algorithm:
    1.As I need to find the least alphabetical order I have to take the largest string with highest alphabetical order
        so, we can take 50 z's let it be 'mostanagarm'
    2.To maintain the highest count variable initiate a variable 'c' with 0
    3.Now for each word in list you have to iterate through the other words.
      So we took nested for loops iterating from 0 till end of the list
    4.every string is anagram of itself which must not be counted here so for that if we come across the same string
      at the same index position then we have to skip it
    5.Now make use of isAnagram function here and if they ara anagrams increment the count
    6.if count>c then put the count value in c and put the string value in mostanagram string
    7.if count=c then check whether the mostanagaram> our string and put the string value in mostanagram string
    8.again make the count variable to 0 for the next iteration of outer loop
    9.once you come out of all the loops return the mostanagram string
     '''

    w='z'*50
    c=0
    for i in range (len(l)):
        count=0
        for j in range (len(l)):
            if i==j:
                continue
            else:
                if isAnagram(l[i],l[j]):
                    count+=1
        if count>c:
            c=count
            w=l[i]
        elif count==c:
            if l[i]<w:
                w=l[i]
        count=0
    return w

print(mostAnagrams(readArray()))


