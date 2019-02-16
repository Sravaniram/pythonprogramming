n=input()
c=1
for x in range(0,len(n)-1):
    if(n[x]==n[x+1]):
        c=c+1
    else:
        if(c>1):
            
            print(c,end=(""))
            print("*",end=(""))
            print(n[x],end=(""))
            c=1
        else:
            print(n[x],end=(""))
if(c>1):
    print(c,end=(""))
    print("*",end=(""))
    print(n[x],end=(""))
    
else:
    print(n[x+1])
