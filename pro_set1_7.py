n=int(input())
k=1
while(k>=1):
    k=k*2
    if(k==n):
        p=0
        break
    if(k>n):
        p=min(abs(k-n),abs(n-int(k/2)))
        break
print(p)
    
