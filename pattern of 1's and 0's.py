o,z=map(int,input().split())
a=[]
if(z==o or z+1==o):
    for x in range(0,z+o):
        if(x%2==0):
            a.append(1)
        else:
            a.append(0)
    s="".join(map(str,a))
    print(s[:z+o])
elif(z==(2*o) or z==(2*o)+2 or z==(2*o)+1):
    for x in range(0,z+1):
        a.append(1) 
        x=x+1 
        a.append(1)
        x=x+1 
        a.append(0)
    s="".join(map(str,a))
    print(s[:z+o])
else:
    print("-1")
