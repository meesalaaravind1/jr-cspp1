def isTidy(n):
    x=10
    while(n>0):
        rem=n%10
        n//=10
        if rem>x:
            return False
        x=rem
    return True

def nthTidyNumber(n):
    c=-1
    num=1
    while c!=n:
        if isTidy(num):
            c+=1
            print (c,num)
        num+=1
    return num-1
print(nthTidyNumber(int(input())))
# print (isTidy(int(input())))