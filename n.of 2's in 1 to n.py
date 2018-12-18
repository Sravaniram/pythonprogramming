n=int(input())
c=0
for x in range(0,n+1):
    while(x!=0):
        a=x%10
        if(a==2):
            c=c+1
        x=int(x/10)
print(c)
