m,n=map(str,input().split())
l=[]
k=[]
c=0
for x in m.lower():
    l.append(x)
for x in n.lower():
    k.append(x)
for x in range(0,len(l)):
    if(l[x]==k[x]):
        c=c+1 
if(c==len(l)):
    print("yes")
else:
    print("no")
