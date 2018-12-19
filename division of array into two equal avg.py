n=int(input())
l=input().split()
k=[]
s=[]
for x in l:
    k.append(int(x))
for x in range(0,len(k)):
    s1=0
    s2=0
    c1=0
    c2=0
    for y in range(x+1,len(k)):
        s1=s1+k[y]
        c1=c1+1
    if(c1>0):
        s1=int(s1/(c1))
    for z in range(0,x+1):
        s2=s2+k[z] 
        c2=c2+1
    if(c2>0):
        s2=int(s2/(c2))
    if(s1==s2):
        print("yes")
        break
else:
    print("no")
