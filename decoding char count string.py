m=input()
s=str()
for x in range(1,len(m)):
    if(m[x].isnumeric()):
        s=s+(m[x-1]*int(m[x]))
print(s)
        
        
