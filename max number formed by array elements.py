s=list(map(int,input().split()))
p=len(str(max(s)))
o=[]
m=[]
for x in range(0,len(s)):
    if(len(str(s[x]))!=p):
        m.append(s[x]*10)
    else:
        m.append(s[x])
while(len(m)>0):
    k=0
    k=m.index(max(m))
    m.remove(max(m))
    o.append(s[k])
    s.remove(s[k])
k1="".join(map(str,o))
print(k1)
