n=input().split()
k=[]
for x in n:
    k.append(x[::-1])
for i in range(0,len(k)):
    if(i==len(k)-1):
        print(k[i],end=(""))
    else:
        print(k[i],end=(" "))
    
