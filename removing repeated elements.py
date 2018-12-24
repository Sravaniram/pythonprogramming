m=input()
n=[]
for x in m:
    if(x not in n):
        n.append(x)
s1="".join(map(str,n))
print(s1)
