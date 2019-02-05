n=int(input())
k=[]
l=list(map(int,input().split()))
for x in range(0,n):
    k.append(l[x])
    if(len(k)<len(l)):
        print(min(k),end=" ")
    else:
        print(min(k))
