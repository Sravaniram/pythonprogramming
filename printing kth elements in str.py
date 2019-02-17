n,m=map(str,input().split())
m=int(m)
k=[]
for x in range(m-1,len(n),m):
    k.append(n[x])
l=" ".join(map(str,k))
print(l)
        
