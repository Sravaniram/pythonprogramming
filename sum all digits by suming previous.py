n=input()
s=0
for x in range(0,len(n)):
    for y in range(0,x+1):
        s=s+int(n[y])
print(s)
