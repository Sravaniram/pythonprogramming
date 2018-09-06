n=int(input())
s=[]
while(n>0):
    a=n%10
    n=n//10
    if(a%2!=0):
        s.append(a)
c=sorted(s)
f=len(c)
for x in range(0,f-1):
    print(c[x],end=(" "))
print(c[f-1])

    
