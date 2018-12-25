def fact(y):
    a=1
    for x in range(1,y+1):
        a=a*x
    return int(a)
m,n=map(int,input().split())
k=fact(m)
p=fact(n)
x=p
while(x>=1):
    if(k%x==0 and p%x==0):
        print(x)
        break
    x=x-1
