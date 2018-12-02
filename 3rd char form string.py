a=str(input())
k=[]
for x in range(0,len(a),3):
    k.append(a[x])
s=''.join(map(str,k))
print(s)
    
