s=input().split()
k=0
for x in s:
    if(k<len(s)):
        if(k%2==0):
            s[k]=x[::-1]
            k=k+1
        else:
            k=k+1
g=" ".join(map(str,s))
print(g)
