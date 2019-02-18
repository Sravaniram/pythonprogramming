n,k=map(eval,input().split())
s=list(map(int,input().split()))
i=0
c=0
while i<len(s):
  if s[i]+k<=5:
    c=c+1
  i=i+1
print(c//3)
