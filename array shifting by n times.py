k1,n=map(int,input().split())
k=input().split()
while(n>0):
    k.insert(0,k.pop())
    n=n-1
for i in range(0,len(k)):
    if(i!=len(k)-1):
        print(k[i],end=(" "))
    else:
        print(k[i])
