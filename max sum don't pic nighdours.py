k=int(input())
l=list(map(int,input().split()))
l.sort()
s=0
for x in range(len(l)-1,-1,-2):
    s=s+l[x]
print(s)
