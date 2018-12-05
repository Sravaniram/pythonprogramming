n=int(input())
a=[]
for x in range(1,n+1):
    if(n%x==0 and x%2!=0):
        a.append(x)
s=" ".join(map(str,a))
print(s)
