a=int(input())
count=0
for x in range(2,a):
    if(a%x==0):
        count=count+1
    else:
        count=count
if(count>0):
    print("yes")
else:
    print("no")
