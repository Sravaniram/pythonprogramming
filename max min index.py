l=input().split()
k=[]
for x in l:
    k.append(int(x))
print(k.index(min(k))+1,k.index(max(k))+1)
