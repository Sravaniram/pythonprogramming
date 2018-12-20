n=int(input())
l=input().split()
s=[]
x,y=map(int,input().split())
for i in l:
    s.append(int(i))
a=s.index(x)
b=s.index(y)
if(a>b):
    print(a-b)
else:
    print(b-a)
