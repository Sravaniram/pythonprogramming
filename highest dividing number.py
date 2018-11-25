m,a=map(int,input().split())
c=0
x=a-1
while(c==0 and x>1):
    if(a%x==0 and m%x==0):
        c+=1
    x-=1
print(x+1)
