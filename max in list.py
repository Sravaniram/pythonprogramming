k=int(input())
n=list(map(int,input().split()))
for x in range(0,k):
    if(n[x]>n[x+1]):
        print(n[x])
        break
