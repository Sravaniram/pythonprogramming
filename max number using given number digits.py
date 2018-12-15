n=input()
k=[]

for x in n:
    k.append(x)
k.sort()
s="".join(map(str,k))
print(s[::-1])
