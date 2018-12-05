s=int(input())
c=0
for x in range(2,s+1):
    if(s%x==0):
        c=c+1
if(c!=0):
    print("yes")
else:
    print("no")
    
