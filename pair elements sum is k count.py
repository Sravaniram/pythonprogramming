m,n=map(int,input().split())
l1=input().split()
l=[]
p=0
for x in l1:
    l.append(int(x))
for x in range(0,len(l)-1):
    for y in range(x,len(l)):
        if(l[x]-l[y]==n or l[y]-l[x]==n):
            p=p+1
print(p)
