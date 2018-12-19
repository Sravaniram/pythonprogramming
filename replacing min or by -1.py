n=int(input())
l=input().split()
k=[]
s=[]
for x in l:
    k.append(int(x))
for x in range(0,len(k)-1):
    if(k[x]>k[x+1]):
        k[x]=k[x+1]
    else:
        k[x]=-1
k[len(l)-1]=-1
o=" ".join(map(str,k))
print(o)
