a=str(input())
c=0
for x in range(0,len(a)):
    if(a[x]=='('):
        c=c+1
    if(a[x]==')'):
        c=c-1
if(c==0):
    print("yes")
else:
    print("no")
