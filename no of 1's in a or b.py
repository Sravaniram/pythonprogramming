n,m=map(int,input().split())
k=format(n | m,"b")
c=0
for y in k:
    if(y=="1"):
        c=c+1 
print(c)
