n=input()
k=list(n)
s=0
for x in range(0,len(k)):
    s=s+(int(k[x])**x)
print(s)
