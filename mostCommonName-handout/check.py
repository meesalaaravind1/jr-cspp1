def occurances(s,sub):
    li=[]
    for i in range(len(s)-len(sub)+1):
        if s[i:len(sub)+i] == sub:
            li.append(i)
    return li

n=int(input())
for k in range(n):
    s=input()
    d={}
    d['KICK']=occurances(s,'KICK')
    # print (d['KICK'])

    d['START']=occurances(s,'START')
    # print (d['START'])
    # li=[(i,j) for i in d['KICK'] for j in d['START'] if i<j]
    c=0
    for i in d['KICK']:
        for j in d['START']:
            if i<j:
                c+=1
    # print ('Case #'+str(i+1)+': '+str(len(li)))
    print ('Case #'+str(k+1)+': '+str(c))
    # start_rindex=s.rindex('START')
    # i=0
    # c=0
    # while(i<len(s)):
    #     if s[i:len('KICK')+i]=='KICK' and i <start_rindex:
    #         c+=1
    #         i+=4
    #     else:
    #         i+=1
    # print ('Case #'+str(k+1)+': '+str(c))
