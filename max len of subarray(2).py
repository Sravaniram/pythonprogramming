n=int(input())
m=list(map(int,input().split()))
c=1
k=[]
for x in range(1,len(m)):
    if(m[x]>=m[x-1]):
        c=c+1
    else:
        k.append(c)
        c=1
k.append(c)
print(max(k))
        
