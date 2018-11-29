a=input().split()
s=" ".join(map(str,a))
k=[]
c=0
for x in s:
    if(x==" "and c<1):
         continue
         c+=1
    else:
        k.append(x)
s1="".join(k)
print(s1)
        
