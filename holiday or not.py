a=str(input())
s=['Monday','Tuesday','wednesday','Thursday','Friday','Saturday']
if(a=='Sunday'):
    print('yes')
else:
    for x in s:
        if(a==x):
            print('no')
