p=int(input())
l=input().split()
a=" ".join(map(str,l))
m=[]
for x in a:
    if(x not in m):
        if(a.count(x)>1):
            m.append(x)
n=" ".join(m) 
print(n[0:2])
