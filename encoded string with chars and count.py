m=input()
n=[]
l=[]
k=[]
for x in m:
    if(x not in n):
        n.append(x)
for y in n:
    l.append(m.count(y))
for x in range(0,len(l)):
    k.append(n[x])
    k.append(l[x])
s="".join(map(str,k))
print(s)
