n=int(input())
l=list(map(int,input().split()))
l=l[::-1]
s="->".join(map(str,l))
'''for x in range(0,len(l)):
    if(x==len(l)-1):
        print(l[x],end=(""))
    else:
        print(l[x],end=("->"))'''
print(s,)
    
