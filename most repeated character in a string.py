s=input()
m=0
d={}
for i in s:
    d={s.count(i):i}
    if(s.count(i)>m):
        m=s.count(i)
print(d[m])
    
