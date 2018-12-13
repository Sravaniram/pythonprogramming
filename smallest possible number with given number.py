n=int(input())
l=[]
while(n>0):
    a=n%10
    n=int(n/10)
    l.append(int(a))
l.sort()
if(0 not in l):
    s="".join(map(str,l))
    print(s)
else:
    l[0],l[1]=l[1],l[0]
    s="".join(map(str,l))
    print(s)
