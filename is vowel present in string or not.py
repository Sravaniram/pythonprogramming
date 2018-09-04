a=str(input())
c=0
for ex in a:
    if((ex=='a'or ex=='e'or ex=='i'or ex=='o'or ex=='u')or(ex=='A'or ex=='E'or ex=='I'or ex=='O'or ex=='U')):
        c=c+1
if(c>0):
    print("yes")
else:
    print("no")
