a=int(input())
s=0
while(a>0):
    a1=int(a%10)
    s=(a1*a1)+s
    a=int(a/10)
print(s)
