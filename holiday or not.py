a=str(input())
s=['Monday','Tuesday','wednesday','Thursday','Friday']
if(a=='Sunday' or 'Saturday' ):
    print('yes')
else:
    for x in s:
        if(a==x):
            print('no')
