a=str(input())
b=(len(a))
c=0
for x in range(0,b):
    if(a[x]==a[b-x-1]):
        c=c+1
if(c==b):
    print("yes")
else:
    print("no")
