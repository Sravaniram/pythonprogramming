n=int(input())
l=input().split()
l1=[]
l2=[]
count=0
for x in l:
    l1.append(int(x))
for i in range(0,len(l1)):
    if l1[i] not in l2:
        l2.append(int(l1[i]))
for x in range(0,len(l2)):
    
    if(count<=l1.count(l2[x])):
        count=l1.count(l2[x])
        a=x
    else:
        count=count
print(l2[a])
        

