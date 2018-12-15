n=int(input())
k=[]
for x in range(2,n):
    for y in range(2,x):
        if(x%y==0):
            break
    else:
        k.append(x)
            
s=" ".join(map(str,k))
print(s)
            
