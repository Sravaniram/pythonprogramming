n=list(map(int,input().split()))
m=list(map(int,input().split()))
for x in m:
    n.append(x)
n.sort()
s=" ".join(map(str,n))
print(s)
