n=int(input())
l1=[]
l=input().split()
for x in l:
    l1.append(int(x))
x=1
while (x<len(l1)):
    if(x%2!=0 and l1[x]>l1[x-1]):
        x=x+1
    elif(x%2==0 and l1[x]<l1[x-1]):
        x=x+1
    else:
        print("no")
        break
else:
    print("yes")
        
    
