n=int(input())
s=list(map(int,input().split()))
k=s.count(s[0])
for x in s:
    if(s.count(x)>k):
        k=s.count(x)
print(k)
        
    
