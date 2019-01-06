s=input()
s2=input()
c=1
for x in range(2,min(len(s),len(s2))+1):
    if(len(s)%x==0 and len(s2)%x==0):
        c=c+1 
print(c)
