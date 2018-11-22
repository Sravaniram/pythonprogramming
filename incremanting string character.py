a=str(input())
b=[]
for x in a:
    if(x=='z' or 'Z'):
        x=chr(ord(x)-23)
        b.append(x)
    else:
        x=chr(ord(x)+3)
        b.append(x)
s=''.join(b)
print(s)
