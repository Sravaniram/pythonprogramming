n,m=map(int,input().split())
p=0
for x in range(2,max(n,m)):
    if(n%x==0 and m%x==0):
        p=p+1 
if(p>1):
    print("yes")
else:
    print("no")
