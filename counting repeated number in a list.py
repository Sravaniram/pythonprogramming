n=int(input())
k=int(input())
s=[]
count=0
for x in range(0,n):
    s.append(int(input()))
for x in s:
    if(x==k):
        count=count+1
print(count)
