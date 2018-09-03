s=str(input())
count=0
for x in s:
    if(x=='1' or x=='0'):
        count=count+1
    else:count=count
if(count==len(s)):
    print("yes")
else:
    print("no")
    
