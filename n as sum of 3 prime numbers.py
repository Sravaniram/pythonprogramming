n=int(input())
a=[]
k=[]
for x in range(2,n):
  i=2
  for i in range(2,x):
    if(x%i==0):
      break
  else:
    a.append(x)
for x in a:
    for y in a:
        for z in a:
            if(int(x)+int(y)+int(z)==n):
                k.append(x)
                k.append(y)
                k.append(z)
for x in range(0,3):
    if(x==2):
        print(k[x])
    else:
        print(k[x],end=(" "))
            
