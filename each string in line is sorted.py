n=input().split()
for x in range(0,len(n)):
    k="".join(sorted(n[x]))
    if(x<len(n)-1):
        print(k,end=(" "))
    else:
        print(k,end=(""))
