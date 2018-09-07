n=int(input())
k=0
while(n>0):
    a=n%10
    n=n//10
    k=k*10+a
print(k)
