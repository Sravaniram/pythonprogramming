a=str(input())
s=[]
for x in a:
    if(x not in s):
        s.append(x)
k="".join(map(str,s))
print(k)
