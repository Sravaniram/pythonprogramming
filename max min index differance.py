m=int(input())
n=list(map(int,input().split()))
for x in range(0,m):
    if(n[x]==min(n)):
        c=x 
        break
for x in range(0,m):
    if(n[x]==max(n)):
        c1=x 
        break
print(abs(c-c1))
