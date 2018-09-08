b,a=map(int,input().split())
l=[]
count=0
if(b<=2<=a):
        l.append(2)
        count=count+1
if(b<=3<=a):
        l.append(3)
        count=count+1
if(b<=5<=a):
        l.append(5)
        count=count+1
if(b<=7<=a):
        l.append(7)
        count=count+1
for x in range(b,a+1):
    if(x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0):
        l.append(x)
        count=count+1
print(count)

