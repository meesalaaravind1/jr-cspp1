def mostCommonName(a):
    maxcount=0
    for i in a:
        if a.count(i)>maxcount:
            maxcount=a.count(i)
    li=[]
    for i in a:
        if a.count(i)==maxcount and i not in li:
            li.append(i)

    return li


print(mostCommonName(input().split(" ")))