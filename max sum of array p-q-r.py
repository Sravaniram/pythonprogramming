n,p,q,r=map(int,input().split())
n=int(n)
p=int(p)
q=int(q)
r=int(r)
l=[]
m=0
l=list(map(int,input().split()))
l.sort()
for i in range(n):
	for j in range(i,n):
            for k in range(j,n):
                s=(p*l[i])+(q*l[j])+(r*l[k])
                if m<s:
                        m=s
print(s)
