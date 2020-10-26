def read2DArray():
    a = []
    l = int(input())
    for i in range(l):
        s = input().split(" ")
        t = []
        for j in range(len(s)):
            t.append(int(s[j]))
        a.append(t)
    return a

def isvalid(i,j,L):
    return i<len(L) and j<len(L[0]) and i>=0 and j >=0

def isKnightsTour(L):
    if len(L)==0:
        return True
    # for i in L:
    #     if len(i)!=len(L):
    #         return False
    else:
        row=0
        col=0
        for i in range(len(L)):
            if 0 in L[i]:
                return False
            if 1 in L[i]:
                row=i
                col=L[i].index(1)
        return check(row,col,1,L)
                #(i+1,j-2),(i+1,j+2),(i-1,j-2),(i-1,j+2),(i+2,j-1),(i-2,j-1),(i+2,j+1),(i-2,j+1)

def check(i,j,val,L):

    if val==(len(L)*len(L[0])):
        return True
    if isvalid(i+1,j-2,L):
        if L[i+1][j-2]==L[i][j]+1:
            return check(i+1,j-2,L[i][j]+1,L)
    if isvalid(i+1,j+2,L):
        if L[i+1][j+2]==L[i][j]+1:
            return check(i+1,j+2,L[i][j]+1,L)
    if isvalid(i-1,j-2,L):
        if L[i-1][j-2]==L[i][j]+1:
            return check(i-1,j-2,L[i][j]+1,L)
    if isvalid(i-1,j+2,L):
        if L[i-1][j+2]==L[i][j]+1:
            return check(i-1,j+2,L[i][j]+1,L)
    if isvalid(i+2,j-1,L):
        if L[i+2][j-1]==L[i][j]+1:
            return check(i+2,j-1,L[i][j]+1,L)
    if isvalid(i+2,j+1,L):
        if L[i+2][j+1]==L[i][j]+1:
            return check(i+2,j+1,L[i][j]+1,L)
    if isvalid(i-2,j-1,L):
        if L[i-2][j-1]==L[i][j]+1:
            return check(i-2,j-1,L[i][j]+1,L)
    if isvalid(i-2,j+1,L):
        if L[i-2][j+1]==L[i][j]+1:
            return check(i-2,j+1,L[i][j]+1,L)

    return False




print(isKnightsTour(read2DArray()))


