n=int(input())
l=list(map(int,input().split()))
m=l[0]
k=[]
k.append(m)
for x in range(1,len(l)):
    m=m+l[x] 
    k.append(m)
    
print(max(k))
