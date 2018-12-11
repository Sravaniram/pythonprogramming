n=int(input())
l11=input().split()
l=[]
for x in l11:
    l.append(int(x))
l.sort()
a=[]
k=int(len(l)/2)
for x in range(0,k):
    a.append(l[len(l)-1-x])
    a.append(l[x])
if(len(l)%2!=0):
    a.append(l[k])
s=" ".join(map(str,a))
print(s)
