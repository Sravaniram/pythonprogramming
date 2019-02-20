m=int(input())
n=list(map(int,input().split()))
for x in range(0,m):
    if(n.count(n[x])==1):
        print(n[x])
        break
        
