n,m=map(str,input().split())
for x in range(len(m)-1,-1,-1):
    if(m[:x+1] in n):
        print(m[:x+1])
        break
