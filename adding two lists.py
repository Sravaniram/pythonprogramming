n=int(input())
l1=input().split()
l2=input().split()
k=[]
for x in range(0,n):
    k.append(int(l1[x])+int(l2[x]))
s=" ".join(map(str,k))
print(s)
