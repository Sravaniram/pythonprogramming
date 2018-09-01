a=int(input())
s=[]
sum=0
for x in range(0,a):
    s.append(int(input()))
    sum=sum+s[x]
print(int(sum/a))
