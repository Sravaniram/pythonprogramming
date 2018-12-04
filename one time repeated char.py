s=input()
p=[]
for x in s:
    if(s.count(x)==1):
        p.append(x)
s1=" ".join(map(str,p))
print(s1)
