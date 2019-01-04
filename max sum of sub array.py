n=int(input())
l=list(map(int,input().split()))
m=l[0]
k=[]
k.append(m)
for x in range(1,len(l)):
    m=m+l[x] 
    k.append(m)
k.append(l[len(l)-1])
a=l[len(l)-1]
for y in range(len(l)-2,-1,-1):
    a=a+l[y] 
    k.append(a)
    
    
print(max(k))
