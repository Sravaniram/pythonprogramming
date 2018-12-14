n,m=map(int,input().split())
c=0
while(n<2):
    n=n+1
for x in range(n,m):
    s=0
    while(x!=0):
        a=int(x%10)
        s=s+a
        x=int(x/10)
    if(s>=2):
        
        for y in range(2,s):
            
            if(s%y==0):
                break
        else:
            c=c+1
print(c)
