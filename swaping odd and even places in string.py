a=str(input())
s=list(a)
for x in range(0,len(a)):
    if(x%2==0):
        s[x],s[x+1]=s[x+1],s[x]
print(''.join(s))
