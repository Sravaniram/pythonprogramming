m,k=map(int,input().split())
l=input().split()
s=[]
for x in range(0,len(l)):
    if(int(l[x])!=k):
        s.append(int(l[x]))
if(len(s)>0):
    n=" ".join(map(str,s))
    print(n)
else:
    print("empty")
    
    
