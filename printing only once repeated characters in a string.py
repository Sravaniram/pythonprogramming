l=str(input())
a=[]
for x in l:
    if(x not in a):
        a.append(x)
print(a)
for x in a:
    if(l.count(x)==1):
        print(x,end=(""))
