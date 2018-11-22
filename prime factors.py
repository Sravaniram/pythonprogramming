a=int(input())
y=[]
for x in range(2,a+1):
    if(a%x==0):
        c=0
        for i in range(1,x+1):
            if(x%i==0):
                c=c+1
        if(c==2):
            y.append(x)
for i in range(0,len(y)):
    if(i==len(y)-1):
        print(y[i])
    else:
        print(y[i],end=(' '))
        
