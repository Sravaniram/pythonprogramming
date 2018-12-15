n=input()
k=[]
for x in range(0,len(n)):
    if(x%2!=0):
        k.append(n[x])
    else:
        k.append(n[x].upper())
for x in k:
    print(x,end=(""))
