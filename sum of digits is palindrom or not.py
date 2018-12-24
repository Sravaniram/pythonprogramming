n=input()
s=0
for x in n:
    s=int(x)+s
s=str(s)
k=s[::-1]
if(s==k):
    print("YES")
else:
    print("NO")
