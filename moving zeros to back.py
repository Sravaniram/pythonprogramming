n=int(input())
m=list(map(int,input().split()))
a=[]
for x in m:
    if(x!=0):
        a.append(x)
while(len(a)!=n):
    a.append(0)
s=" ".join(map(str,a))
print(s)
