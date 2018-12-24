n=int(input())
l=input().split()
k=[]
for x in range(0,len(l)):
    k.append(int(l[x]))
    if((x+1)*k[x]==k[x]):
        print(k[x])
        break
else:
    print("0")
