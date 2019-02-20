k,l=map(int,input().split())
l1=list(map(int,input().split()))
if(l in l1):
    print("yes",l1.count(l))
else:
    print("no")
