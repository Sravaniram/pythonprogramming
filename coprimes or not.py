n,m=map(int,input().split())
p=0
if(n==2 and m==3):
    p=p+1
for x in range(2,max(n,m)):
    if(n%x==0 and m%x==0):
        p=p+1 
if(p>0):
    print("yes")
else:
    print("no")
