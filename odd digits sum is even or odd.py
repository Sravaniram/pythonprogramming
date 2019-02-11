n=int(input())
i=0 
s=0
while(n>0):
    i=n%10
    if(i%2!=0):
        s=s+i
    n=n//10
if(s%2==0):
    print("E")
else:
    print("O")
        
