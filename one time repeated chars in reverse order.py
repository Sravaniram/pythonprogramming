s=str(input())
k=[]
for x in s:
    if(x not in k):
        k.append(x)
k.reverse()
l="".join(map(str,k))
print(l)
