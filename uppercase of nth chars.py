k,l=map(str,input().split())
l=int(l)
k1=[]
for x in range(0,len(k)):
    if((x+1)%l==0):
        k1.append(k[x].capitalize())
    else:
        k1.append(k[x])
f="".join(map(str,k1))
print(f)
    
