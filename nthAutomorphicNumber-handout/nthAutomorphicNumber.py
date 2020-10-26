# def countdigit(n):
#     if n==0:
#         return 1
#     c=0
#     while n>0:
#         n=n//10
#         c+=1
#     return c

def isAutomorphic(n):
    x=n*n
    while n>0:
        if x%10 != n%10:
            return False
        x=x//10
        n=n//10
    return True


def nthAutomorphicNumber(n):
    c=-1
    x=-1
    while c<n:
        if isAutomorphic(x):
            c+=1
            print (c,x)
        # print (x)
        x+=1
    return x-1
print(nthAutomorphicNumber(int(input())))
# print (isAutomorphic(int(input())))





