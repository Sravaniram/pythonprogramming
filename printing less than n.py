n=int(input())
c=[]
l=list(map(int,input().split()))
for x in l:
    if(x<n):
        c.append(x)
for y in range(0,len(c)):
    if(y==len(c)-1):
        print(c[y])
    else:
        print(c[y],end=" ")
