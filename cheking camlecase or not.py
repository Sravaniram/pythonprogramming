l=input()
c=-1
k=0
if(l[0]>="A" and l[0]<="Z"):
    c=c+1
for x in range(0,len(l)):
    if(l[x]==" "):
        k=k+1
        if(l[x+1]<="Z" and l[x+1]>="A"):
            c=c+1 
if(k==c):
    print("yes")
else:
    print("no")
    
