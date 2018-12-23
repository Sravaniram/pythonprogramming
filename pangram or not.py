a=input()
k=[]
for x in a:
    if(x not in k):
        k.append(x)
if(len(k)==27 or len(k)==28):
    print("yes")
else:
    print("no")
