n=int(input())
l=list(map(int,input().split()))
s=0
l.sort()
for x in range(0,n-1):
    s=s+l[x] 
    if(s>l[x+1]):
        break
print(x+2)
        
