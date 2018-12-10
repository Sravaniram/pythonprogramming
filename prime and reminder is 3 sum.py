n=int(input())
s=0
for x in range(1,n+1):
    if(x%2!=0 and x%10==3):
        s=s+x
print(s)
