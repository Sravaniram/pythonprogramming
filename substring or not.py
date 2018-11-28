i,j=map(int,input().split())
s=input().split()
l=input().split()
s.sort()
l.sort()
s1=''.join(s)
s2=''.join(l)
if(s2 in s1):
    print("YES")
else:
    print("NO")
