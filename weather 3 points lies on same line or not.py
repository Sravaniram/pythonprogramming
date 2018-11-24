x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
if((x1==x1==x3) or (y1==y2==y3)):
    print("yes")
elif(((y2-y1)/(x2-x1))==((y3-y1)/(x3-x1))):
    print("yes")
else:
    print("no")
