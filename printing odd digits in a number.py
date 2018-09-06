n=int(input())
s=[]
while(n>0):
    a=n%10
    n=n//10
    if(a%2!=0):
        s.append(a)
c=sorted(s)
for x in c:
    print(x,end=(" "))

    
