a,b=map(str,input().split())
c=0
for x in range(0,len(a)):
    if((ord(a[x])-ord(a[x-1]))!=(ord(b[x])-ord(b[x-1]))):
        c=c+1
if(c>0):
    print("no")
else:
    print("yes")
