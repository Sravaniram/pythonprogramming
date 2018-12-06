n,k=map(str,input().split())
c=1
for x in n:
    if(k==x):
        print(c)
        break
    else:
        c=c+1
