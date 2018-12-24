m=input()
n=[]
for x in m:
    if(x not in n):
        n.append(x)
s="".join(map(str,n))
print(s)
