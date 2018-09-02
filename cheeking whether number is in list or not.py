a=int(input())
b=int(input())
s=[]
count=0
for x in range(0,a):
    s.append(int(input()))
for x in range(0,len(s)):
    if(s[x]==b):
        count=count+1
    else:
        count=count
if(count>0):
    print("yes")
else:print("no")
    
