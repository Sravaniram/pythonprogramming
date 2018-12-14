n=input()
s=0
for x in range(0,len(n)):
    s=s+int(n[x])**len(n)
print(s)
