m=input()
count=0
for x in range(0,len(m)):
    if(m[x].isdigit() or m[x].isalpha() or m[x]==" "):
        count=count
    else:
        count=count+1
print(count)
