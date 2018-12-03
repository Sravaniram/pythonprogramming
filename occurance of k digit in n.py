m,n=map(int,input().split())
c=0
while(m!=0):
    m1=m%10
    if(m1==n):
        c=c+1
    m=int(m/10)
print(c)
