l=input().split()
k=int(input())
s=[]
for x in range(0,len(l)):
    if(int(l[x])!=k):
        s.append(int(l[x]))
if(len(s)>0):
    n=" ".join(map(str,s))
    print(n)
else:
    print("empty")
    
    
