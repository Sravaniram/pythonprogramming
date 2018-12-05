def rat(s,n):
    print(s[n:]+s[:n])
s,n=map(str,input().split())
n=int(n)
m=len(s)-n
rat(s,m)
