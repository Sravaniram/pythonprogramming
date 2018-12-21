n=int(input())
p=input().split()
l=[]
for x in p:
    l.append(int(x))
print(max(l)-min(l))
   
