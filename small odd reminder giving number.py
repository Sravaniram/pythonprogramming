n=int(input())
for x in range(1,n):
    a=int(n/x)
    if(a%2!=0 and n%x==0):
        print(x)
        break
else:
    print(n)
    
