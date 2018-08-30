a=input()
try:
  i=float(a)
except(ValueError,TypeError):
    print("No")
else:    
    print("Yes")
