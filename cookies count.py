n,m=map(int,input().split())
m1=list(map(int,input().split()))
m2=list(map(int,input().split()))
s1=0
s2=0
for x in range(0,len(m1)):
    s1=s1+m1[x]
    s2=s2+m2[x]
print(s2//s1)
