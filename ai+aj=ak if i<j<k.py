n=int(input())
c=0
m=list(map(int,input().split()))
for x in range(0,n-2):
    for y in range(x+1,n-1):
        for z in range(y+1,n):
            if(m[x]+m[y]==m[z]):
                c=c+1
    
print(c)
    
    
    
