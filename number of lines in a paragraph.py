n=input()
count=1
for x in range(0,len(n)):
    if(n[x]=="."):
        count=count+1
    else:
        count=count
print(count)
