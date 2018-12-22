m=int(input())
l=input().split()
n=input()
k=len(n)
c=0
for x in l:
    if(x[:k]==n):
        c=c+1
print(c)
    
