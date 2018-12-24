n,m=map(int,input().split())
a=[]
c=0
k=['a','e','i','o','u','A','E','I','O','U']
for x in range(0,n):
    a.append(str(input()))
    for y in a[x]:
        if(y in k):
            c=c+1
            break
if(c>=m):
    print("yes")
else:
    print("no")
