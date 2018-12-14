n,m=map(str,input().split())
n1=list(n)
m1=list(m)
x=1
while(len(n1)-len(m1)!=0):
    if(len(n1)>len(m1)):
        m1.append(x)
        x=x+1
    else:
        n1.append(x)
        x=x+1
for x in range(0,len(n1)):
    print(n1[x],end=(""))
    print(m1[x],end=(""))

