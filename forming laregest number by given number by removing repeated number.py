n=int(input())
l=[]
while(n!=0):
    l.append(int(n%10))
    n=int(n/10)
for x in range(0,len(l)-1):
    if(l[x]==l[x+1]):
        del(l[x])
        break
s="".join(map(str,l))
print(s[::-1])
