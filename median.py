n=int(input())
l=[]
for x in range(0,n):
    l.append(int(input()))
a=sorted(l)
b=len(l)
c=int(b/2)
if(b%2==0):
   print(a[c-1],a[c])
else:
    print(a[c])
