n,m=map(int,input().split())
l=list(map(int,input().split()))
s1,s2=[],[]
if n%2!=0:
	s1=l[:n-1]
	s2=l[n-1:n]
else:
	s1=l[:n//2]
	s2=l[n//2:n]
print(max(min(s1),min(s2)))
