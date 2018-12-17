n,m=map(int,input().split())
l1=[]
l=input().split()
for x in l:
    l1.append(int(x))
l1.sort()
s=" ".join(map(str,l1))
print(s)
