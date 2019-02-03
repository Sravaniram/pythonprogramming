n=int(input())
l=[]

k=list(map(int,input().split()))
p=len(k)
if(p<=3):
    print(k[2])
else:
    while(p>3):
        for x in range(0,p):
            if(x%2!=0):
                k[x]=0
        for y in k:
            if(y>0):
                l.append(y)
        k.clear()
        k=l.copy()
        p=len(k)
    print(k[1])
