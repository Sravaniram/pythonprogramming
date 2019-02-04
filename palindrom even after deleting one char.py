s=input()

for y in range(0,len(s)):
    k=s[:y]+s[y+1:]

    if(k[:]==k[::-1]):
    
        print("YES")
        break
else:
    print("NO")
