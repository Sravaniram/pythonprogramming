m,n=map(int,input().split())
l=input().split()
k=[]
c=0
for x in l:
    k.append(int(x))
for x in k:
    if(x<=n):
        c=c+1
print(c)

