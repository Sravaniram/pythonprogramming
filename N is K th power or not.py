m,n=map(int,input().split())
c=0
for x in range(1,m+1):
    if(m==(n**x)):
        c=c+1
        break
if(c==1):
    print("yes")
else:
    print("no")
