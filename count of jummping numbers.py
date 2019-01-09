x=int(input())
c=1
for y in range(1,x+1):
    if(len(str(y))==1):
        c=c+1
    else:
        s=str(y)
        for e in range(0,len(s)-1):
            if(s[e]=='9' and s[e+1]=='0'):
                c=c+1
            if(s[e]=='0' and s[e+1]=='9'):
                c=c+1
            if(int(s[e])-int(s[e+1])==1 or int(s[e])-int(s[e+1])==-1):
                c=c+1
print(c)
