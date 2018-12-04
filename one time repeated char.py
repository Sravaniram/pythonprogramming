s=input()
s2=str(s.lower())
print(s2)
p=[]
for x in s2:
    if(s2.count(x)==1):
        p.append(x)
s1=" ".join(map(str,p))
print(s1)
