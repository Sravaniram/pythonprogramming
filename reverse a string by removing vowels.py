a=int(input())
s=str(input())
b=[]
for x in s:
    if(x!=('a'or'e'or'i'or'o'or'u')):
        b.append(x)
print(b)
b.reverse()
print(b)
c=''.join(b)
print(c)
