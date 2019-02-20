m=int(input())
n=list(map(int,input().split()))
k=[]
for x in range(0,m):
    if(n[x] not in k):
        k.append(n[x])
k1=" ".join(map(str,k))
print(k1)
    
