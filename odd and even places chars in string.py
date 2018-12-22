n=str(input())
k=[]
p=[]
for x in range(0,len(n)):
    if(x%2==0):
        k.append(n[x])
    else:
        p.append(n[x])
s1="".join(map(str,k))
s2="".join(map(str,p))
print(s1,s2)
