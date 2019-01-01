n,m=map(int,input().split())
l=list(map(int,input().split()))
k=[]
for x in range(0,m):
    i,j=map(int,input().split())
    s=0
    for y in range(i,j+1):
        s=s+l[y]
    k.append(s)
for x in k:
    print(x)
