n=int(input())
l=[]
for x in range(0,2**n):
    l.clear()
    l.append(format(x,"b"))
    s="".join(map(str,l))
    while(len(s)!=n):
        s='0'+s
    if(x!=(2**n)-1):
        print(s,end=("\n"))
    else:
        print(s)
