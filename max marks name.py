n=input()
m=input()
a1,a,b=[],[],[]
ad1,ad2=0,0
for x in n:
    if(x.isnumeric()):
        a.append(int(x))
for y in m:
    if(y.isnumeric()):
        b.append(int(y))
s1="".join(map(str,a))
s2="".join(map(str,b))
for x in range(0,len(s1),2):
    ad1=ad1+int(s1[x:x+2])
    ad2=ad2+int(s2[x:x+2])
if(ad1>ad2):
    x=0
    while(n[x]!="#"):
        a1.append(n[x])
        x=x+1
    s11="".join(map(str,a1))
    print(s11)
else:
    x=0
    while(m[x]!="#"):
        a1.append(m[x])
        x=x+1
    s11="".join(map(str,a1))
    print(s11)
