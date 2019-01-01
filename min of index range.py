n,m=map(int,input().split())
l=list(map(int,input().split()))
k=[]
for x in range(0,m):
    i,j=map(int,input().split())
    s=0
    mi=l[i-1]
    for y in range(i-1,j):
        if(l[y]<mi):
            mi=l[y]
    print(mi)
        
