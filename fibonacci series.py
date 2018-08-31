f=int(input())
a=[]
a.append(1)
a.append(1)
for x in range(2,f):
    a.append(a[x-1]+a[x-2])
print(a[x])
        
