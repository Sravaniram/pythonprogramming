m=[]
n=[]
k=int(input())
for x in range(k):
    n.append(input().split())
for x in n:
    for y in x:
        m.append(int(y))
m.sort()
s=" ".join(map(str,m))
print(s)
