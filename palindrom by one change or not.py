a=str(input())
for x in range(0,len(a)):
    if(a.count(x)==2):
        
        print("yes")
        
        break
else:
    print("no")
