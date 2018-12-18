s=str(input())
a=[]
k=[]
c=1
for x in range(0,len(s)-1):
    if(s[x]==s[x+1]):
        c=c+1
    else:
        k.append(s[x])
        a.append(c)
        c=1
k.append(s[x])
a.append(c)
m=a[0]
for x in range(0,len(k)):
    if(m<=a[x]):
        m=a[x]
        l=x
print(k[l],a[l])
    
