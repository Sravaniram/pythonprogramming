n=int(input())
l=list(map(int,input().split()))
m=max(l)
for x in range(0,n):
    for y in range(x,n):
        if(l[x]<l[y]):
            l[x],l[y]=l[y],l[x]
for x in l:
    print(x)
