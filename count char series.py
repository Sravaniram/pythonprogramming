n=input()
c=1
k=[]
for x in range(0,len(n)-1):
    if(n[x]==n[x+1]):
        c=c+1
    else:
        if(c>1):
            
            k.append(c)
            k.append("*")
            k.append(n[x])
            c=1
        else:
            k.append(n[x])
if(c>1):
    k.append(c)
    k.append("*")
    k.append(n[x])
    
else:
    k.append(n[x+1])
s="".join(map(str,k))
print(s)
