n=int(input())
s=input().split()
c=1
for x in range(0,len(s)-1):
    if(s[x]<=s[x+1]):
        c=c+1
if(c==len(s)):
    print("yes")
else:
    print("no")
