a,b=input().split()
b=int(b)
c=len(a)
d=[]
for i in range(0,c):
	s=a[i]
	d.append(s)
w=c-b
z=[]
for i in range(b,c):
	s=d[i]
	z.append(s)
print("".join(z))
