n,k=map(str,input().split())
c=0
for y in k:
    for x in n:
        if(y==x):
            c=c+1 
if(c>0):
    print("yes")
else:
    print("no")
