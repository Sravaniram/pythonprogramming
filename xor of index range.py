n,m=map(int,input().split())
l=list(map(int,input().split()))
for x in range(0,m):
    i,j=map(int,input().split())
    s=0
    for y in range(i-1,j):
        s=s^l[y]
    print(s)
        
