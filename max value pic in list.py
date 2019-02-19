n,W1=map(int,input().split())
wt=list(map(int,input().split()))
val=list(map(int,input().split()))
ratio=[]
for i in range(n):
  ratio.append(val[i]/wt[i])
cost=0
while W1>=0 and len(ratio)>0:
  if W1>=wt[ratio.index(max(ratio))]:
    cost+=val[ratio.index(max(ratio))]
    W1-=wt[ratio.index(max(ratio))]
  val.pop(ratio.index(max(ratio)))
  wt.pop(ratio.index(max(ratio)))
  ratio.pop(ratio.index(max(ratio)))
print(cost)
