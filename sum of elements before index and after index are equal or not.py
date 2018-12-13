n=int(input())
l1=input().split()
l=[]
for x in l1:
    l.append(int(x))
for x in range(1,n):
    s1=0
    s2=0
    j=x+1
    while(j<=n-1):
        s1=s1+int(l[j])
        j+=1
    i=x-1
    while(i>=0):
        s2=s2+int(l[i])
        i-=1
    if(s1==s2):
        print("yes")
        break
else:
    print("no")
