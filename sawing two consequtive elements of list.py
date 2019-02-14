k=int(input())
n=list(map(int,input().split()))
for x in range(0,k-1,2):
    n[x],n[x+1]=n[x+1],n[x]
s=" ".join(map(str,n))
print(s)
