n=int(input())
count=0
while(n>0):
    a=int(n%10)
    n=int(n/10)
    count=count+a
print(count)
