n=int(input())
l,c=[],0
p=[]
for x in range(1,n+1):
    if(n%x==0):
        l.append(x)
for x in l:
    c=0
    for y in range(1,x+1):
        if(x%y==0):
            c=c+1 
    if(c==2):
        p.append(x)
print(" ".join(str(i) for i in p)) 
