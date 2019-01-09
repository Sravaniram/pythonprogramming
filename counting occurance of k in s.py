x=list(map(str,input().split()))
k=int(x[0])
l=int(x[1])
c=0
for x1 in range(k,l+1):
    if(x[2] in str(x1)):
        c=c+1 
print(c)
