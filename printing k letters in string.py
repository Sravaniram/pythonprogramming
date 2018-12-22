n=input().split()
x=int(n[1])
y=str(n[0])
for i in range(0,len(y)-x+1):
    if(i<len(y)-x):
        for j in range(i,i+x):
            if(j<i+x-1):
                print(y[j],end=(""))
            else:
                print(y[j],end=(" "))
    else:
        for j in range(i,i+x):
            if(j<i+x-1):
                print(y[j],end=(""))
            else:
                print(y[j],end=(""))
        
