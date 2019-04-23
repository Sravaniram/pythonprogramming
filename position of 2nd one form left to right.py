n,m=map(int,input().split())
k=bin(n*m)
c,p=0,1
for x in range(2,len(k)):
    c=c+1
    if(k[x]=='1'):
        if(p==2):
            print(c)
            break
        p=p+1
