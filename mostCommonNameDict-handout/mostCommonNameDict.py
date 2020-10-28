def readList():
    return input().split()

def mostCommonNameDict(L):
    # your code goes here
    if len(L)==0:
        return ""
    s=list()
    d={}
    maxi=0
    for i in L:
        if i not in d:
            d[i]=L.count(i)
            if d[i]>maxi:
                maxi=d[i]
    for i in d:
        if d[i]==maxi and i not in s:
            s.append(i)
    if len(s)>0:
        return (sorted(s))
    else:
        return None

d = mostCommonNameDict(readList())

if d == None:
	print(None)
elif type(d) == set:
	print(sorted(d))
else:
	print(d)
