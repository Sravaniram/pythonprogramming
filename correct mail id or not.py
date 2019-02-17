n=input()
if(n.count("@")==1 and n.count("&")<=1 and n.count(".")<=1 and 'com' in n):
    x,c1,c2=0,0,0
    while(n[x]!='@'):
        c1=c1+1
        x=x+1
    x=x+1
    if(c1>=4):
        while(n[x]!="."):
            c2=c2+1 
            x=x+1 
    if(c2==5):
        print("YES")
    else:
        print("NO")
else:print("NO")
