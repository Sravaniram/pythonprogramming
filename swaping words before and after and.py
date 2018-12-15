n=input().split()
if(len(n)==1):
    print(n[0])
else:
    for x in range(0,len(n)):
        if(n[x]=='and'):
            n[x-1],n[x+1]=n[x+1],n[x-1]
    p=" ".join(map(str,n))
    print(p)
