m,n=map(int,input().split())
l=input().split()
l.sort()
for x in range(0,len(l)-1):
    if(int(l[x])==n):
        print(l[x+1])
        break
