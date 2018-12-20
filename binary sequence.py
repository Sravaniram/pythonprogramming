n=int(input())
l=[]
for x in range(0,2**n):
    l.clear()
    l.append(format(x,"b"))
    s="".join(map(str,l))
    while(len(s)!=n):
        s='0'+s
    print(s)
