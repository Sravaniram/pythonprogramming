n=input()
y=0
k=[]
for x in range(0,len(n)):
    if(n[x].isspace()):
        y=y
        k.append(n[x])
    elif(y%2!=0):
        k.append(n[x])
        y=y+1
    else:
        k.append(n[x].upper())
        y=y+1
s="".join(map(str,k))
print(s)
