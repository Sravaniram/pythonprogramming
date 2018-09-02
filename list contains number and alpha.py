b1=str(input())
s=0
d=0
for x in b1:
    if(x.isalpha()):
        s=s+1
for y in b1:
    if(y.isnumeric()):
        d=d+1
if(d>0 and s>0):
    print("Yes")
else:
    print("No")
