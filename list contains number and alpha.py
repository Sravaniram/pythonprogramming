a1=str(input())
s=0
d=0
for x in a1:
    if(x.isalpha()):
        s=s+1
for y in a1:
    if(y.isnumeric()):
        d=d+1
if(d>0 and s>0):
    print("Yes")
else:
    print("No")
