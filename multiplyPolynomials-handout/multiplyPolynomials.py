def readArray():
    a = input().split(" ")
    l = []
    for i in a:
        l.append(int(i))
    return l

def multipolynomials(p1, p2):
    # Your code goes here
    prod=[0]*(len(p1)+len(p2)-1)
    # print (prod)
    for i in range(len(p1)):
        for j in range(len(p2)):
            prod[i+j]+=p1[i]*p2[j]
    return prod



print(multipolynomials(readArray(), readArray()))