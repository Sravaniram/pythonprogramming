m=int(input())
l1=input().split()
l=[]
p=0
for x in l1:
    l.append(int(x))
for x in l:
    if(l.count(x)==1):
        print(x)
