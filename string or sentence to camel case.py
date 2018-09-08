str=input()
a=list(str)
b=[]
b.append(a[0].upper())
for x in range(1,len(a)):
    if(a[x]==' '):
        b.append(a[x])
        a[x+1]=a[x+1].upper()
    else:
        b.append(a[x])
print(''.join(b))
