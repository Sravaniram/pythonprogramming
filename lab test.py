x=int(input())
x1=list(map(str,input().split()))
for s in x1:
    if(s=='0' or s=='78' or s=='4'):
        print("+")
    if(s[len(s)-2:len(s)]=='35'):
        print("-")
    if(s[1]=='9' and s[len(s)=='4']):
        print("?")
    if(s[0:3]=='190'):
        print("*")
