n,m=map(int,input().split())
k=bin(n*m)
c=0
for x in range(len(k)-1,1,-1):
    c=c+1
    if(k[x]=='1'):
        print(c)
        break
