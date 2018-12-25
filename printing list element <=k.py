m,n=map(int,input().split())
l=input().split()
l1=[]
for x in l:
    l1.append(int(x))
l1.sort()
for x in range(0,len(l1)):
    if(len(l1)>1 and l1[x+1]>n):
        print(l1[x])
        break
else:
    print(l[0])
