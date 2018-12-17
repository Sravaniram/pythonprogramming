n=int(input())
x=1
c=0
while(x>0 and c==0):
    s=0
    y=x
    while(y>0):
        a=int(y%10)
        s=s+a
        y=int(y/10)
    if(s==n):
        print(x)
        c=c+1
    else:
        x=x+1
            
