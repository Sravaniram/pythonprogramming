a=str(input())
b=[]
for x in a:
    x=chr(ord(x)+3)
    b.append(x)
s=''.join(b)
print(s)
