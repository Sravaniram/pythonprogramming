a=str(input())
l=[]
b=['d','h','o','n','i']
b.sort()
for x in a:
    l.append(x)
l.sort()
if(b==l):
    print("yes")
else:
    print("no")
