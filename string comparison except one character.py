a,b=map(str,input().split())
count=0
for x in range(0,len(a)):
    c=a[x]
    d=b[x]
    if(c==d):
        count=count
    else:
        count=count+1
if(count==1):
    print("yes")
else:
    print("no")
        
