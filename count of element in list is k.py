n,m=map(int,input().split())
l=list(map(int,input().split()))
for x in l:
    if(l.count(x)==m):
        print(x)
        break
