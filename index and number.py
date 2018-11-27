a=int(input())
b=input().split()
c=len(b)
p=[]
for i in range(0,c):
	if i%2==0:
		b[i]=int(b[i])
		if b[i]%2!=0:
			p.append(b[i])
	else:
		b[i]=int(b[i])
		if b[i]%2==0:
			p.append(b[i])
s=''.join(map(str,p))
print(s)
