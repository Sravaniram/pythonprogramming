n=int(input())
a=[]
c=0
k=['a','e','i','o','u','A','E','I','O','U']
for x in range(0,n):
    a.append(str(input()))
    for y in a[x]:
        if(y in k):
            c=c+1
if(c>0):
    print("yes")
else:
    print("no")
