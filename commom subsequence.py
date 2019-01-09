n=input()
m=input()
a=[]
for x in n:
    if(x in m and x not in a):
        a.append(x)
k="".join(map(str,a))
print(k)
