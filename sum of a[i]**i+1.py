n=input()
s=0
l=2
if(len(n)>1):
    for x in range(0,len(n)):
        if(l<=len(n)):
            s=s+int(n[x])**l
            l=l+1
        else:
            s=s+int(n[x])**1
else:
    s=int(n[0])**2
        
        
print(s)
    
