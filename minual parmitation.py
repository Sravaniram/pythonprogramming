n = int(input())
L = list(map(int,input().split()))
Lno = []
Ldup = []
Lin = []
for i in range(1,n+1) :
    if i not in L :
        Lno.append(i)
for i in L :
    if L.count(i) > 1 and i not in Ldup :
        Ldup.append(i)
for i in range(0,n) :
    if L[i] in Ldup :
        Lin.append(i)
out = len(Lno)
for i in range(0,n) :
    if len(Lno) == 0 :
        break
    if i in Lin :
        if i == Lin[0] :
            if Lno[0] < L[i] :
                L[i] = Lno.pop(0)
                Lin.pop(0)
            elif L[i] in Ldup :
                Lin.pop(0)
                Ldup.remove(L[i])
            else :
                L[i] = Lno.pop(0)
                Lin.pop(0)
print(out)
print(*L)

    
    
