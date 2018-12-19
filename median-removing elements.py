n=int(input())
l=[]
s=input().split()
for x in s:
    l.append(int(x))
x=len(l)
while(len(l)>0):
    if(len(l)%2==0):
        k=l[int(len(l)/2)]+l[int(len(l)/2)-1]
        print(int(k/2))
        x=int(len(l)/2)
        del(l[x-1:x+1])
    else:
        print(l[int(len(l)/2)])
        del(l[int(len(l)/2)])
        
        
