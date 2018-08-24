n=int(input())
s=n
arm=0
while(n>0):
    a=n%10
    arm=arm+(a**3)
    n=n//10
if(arm==s):
    print("yes")
else:
    print("no")
    
