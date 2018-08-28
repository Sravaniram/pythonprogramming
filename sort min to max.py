import heapq
n=int(input())
a=[]
for x in range(0,n):
    a.append(int(input()))
print(heapq.nsmallest(len(a),a))
