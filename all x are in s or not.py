n,m=map(str,input().split())
m=int(m)
c=0
for x in range(0,m+1):
    p=str(x)
    if(p in n):
        c=c+1 
if(c==m):
    print("yes")
else:
    print("no")
