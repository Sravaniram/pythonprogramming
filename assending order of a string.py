i=int(input())
s=input().split()
a=[]
x=0
l=int(len(s))
for x in range(0,len(s)):
    a.append(s[x])
a.sort()
for x in a:
    if(x==a[len(s)-1]):
        print(x)
    else:
        print(x,end=(" "))
    
    
