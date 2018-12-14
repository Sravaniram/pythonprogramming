n=int(input())
l=input().split()
c=0
for x in range(n-1,-1,-1):
    for y in range(0,x+1):
        if(l[x]>l[y]):
            c=c+1
print(c)
