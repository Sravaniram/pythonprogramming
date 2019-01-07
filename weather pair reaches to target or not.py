x,y=map(int,input().split())
c=0
n=list(map(int,input().split()))
for i in range(0,x):
    for j in range(i,x):
        if(y==n[i]+n[j]):
            c=c+1
if(c>1):
    print("YES")
else:
    print("NO")
