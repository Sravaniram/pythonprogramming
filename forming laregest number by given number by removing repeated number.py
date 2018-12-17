n=int(input())
l=[]
while(n!=0):
    l.append(int(n%10))
    n=int(n/10)
print(l)
for x in range(0,len(l)-3):
    if(l[x]==l[x+1] and l[x]<=l[x+2]):
        del(l[x])
        break
    if(l[x]==l[x+1] and l[x]>=l[x+2]):
        del(l[x+2])
        break
s="".join(map(str,l))
print(s[::-1])
