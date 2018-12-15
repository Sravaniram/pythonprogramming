import sys
n=input().split()
k=[]
for x in n:
    k.append(x[::-1])
sys.stdout.write(k)
    
