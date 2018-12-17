n=int(input())
a=[]
c=0
c1=[]
for x in range(2,n):
    for y in range(2,x):
        if(x%y==0 and c>1):
            break
    else:
        a.append(x)
        c=c+1
for x in range(0,len(a)):
    for y in range(x,len(a)):
        if(a[x]+a[y]==n):
            c1.append(a[x])
            c1.append(a[y])
print(c1[0],c1[1])
                    
