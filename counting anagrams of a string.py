x=int(input())
s=[]
c=0
s1='kabali'
for k in range(0,x):
    s.append(str(input()))
for k in range(0,x):
    if(sorted(s[k])==sorted(s1)):
        c=c+1
print(c)
