n=int(input())
s=0
a=list(map(int,input().split()))
for y in range(0,n):
    for x in range(0,y):
        if(a[x]<a[y]):
            s=s+a[x]
print(s)
            
