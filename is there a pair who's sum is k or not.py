n,m=map(int,input().split())
k=list(map(int,input().split()))
c=0
for x in range(0,n):
    for y in range(0,x):
        if(k[x]+k[y]==m):
            c=c+1
if(c>0):
    print("yes")
else:
    print("no")
