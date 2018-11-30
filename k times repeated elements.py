l=input().split()
n=int(l[2])
c=0
s="".join(map(str,l[0]))
s1="".join(map(str,l[1]))
for x in range(0,len(s)):
    if(s[x]!=s1[x]):
        c=c+1
if(c==n):
    print("yes")
else:
    print("no")
