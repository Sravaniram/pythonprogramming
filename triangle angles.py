l=input().split()
c=0
p=0
for x in l:
    if(int(x)==0):
        c=c+1
if((int(l[0])+int(l[1])+int(l[2]))==180):
    p=p+1
if(p==1 and c==0):
    print("yes")
else:
    print("no")
