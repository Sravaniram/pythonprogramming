a=input()
k=[]
for x in a:
    if(x not in k):
        k.append(x)
if(len(k)==27):
    print("yes")
else:
    print("no")
