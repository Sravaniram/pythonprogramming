n,m=map(int,input().split())
k=list(map(int,input().split()))
c=0

while(len(k)!=0):
    if(max(k)<m):
        c=c+int(m//max(k))
        m=m%max(k)
        k.remove(max(k))
    elif(max(k)>m):
        k.remove(max(k))
    else:
        c=c+1 
        break
print(c)
