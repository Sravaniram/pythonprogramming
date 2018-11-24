a,b=map(int,input().split())
x=1
c=0
while(c<1 and x>=1):
    if(x%a==0 and x%b==0):
        c=c+1
    x=x+1
print(x-1)
