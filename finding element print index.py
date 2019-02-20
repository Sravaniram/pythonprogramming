n=list(map(str,input().split()))
k=input()
for x in range(0,len(n)):
    if(n[x]==k):
        print(x+1)
        break
