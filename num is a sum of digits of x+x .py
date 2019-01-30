n=int(input())
k=1 
c=1
while(k<n):
    p=k 
    s=0
    while(p>0):
        o=(p%10)
        s=s+o
        p=int(p/10)
    if(s+k==n):
        print("1")
        print(k)
        c=0
        break
    else:
        k=k+1
if(c==1):
    print("0")


