def readArray():
    l = input().split(" ")
    r = []
    for i in l:
    	r.append(int(i))
    return r

def repeatingPattern(l):
    '''
    take and empty list
    find the repeating pattern and put it in b
    find the k value and check whether k*b == a
    '''
    b=[]
    for i in l:
        if i not in b:
            b.append(i)
        else:
            break
    k=2
    while(k<10):
        if b*k==l:
            return True
        k+=1
    return False


print(repeatingPattern(readArray()))


