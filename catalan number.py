def fact(l):
    m=1
    for x in range(1,l+1):
        m=m*x
    return m

n=int(input())
a=[]
i=0
while(i<=n):
    if(i==0):
        a.append(1)
     else:
        a.append(fact(2*i)//((fact(i+1))*fact(i)))
     i=i+1
p=" ".join(map(str,a))
print(p)
        
