m=input().split()
s="".join(m)
for x in range(2,len(s)):
    if(len(s)%x==0):
        print("no")
        break
else:
    print("yes")
    
