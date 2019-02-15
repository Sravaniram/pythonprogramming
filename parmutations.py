from itertools import permutations 
l=list(input()) 
p = permutations(l) 
a=[]  
for i in list(p):
  s='' 
  for j in i:
    s+=j
  if s not in a:
    a.append(s)
    print(s)

