x=list(map(int,input().split()))
c=0
while x[0]<=x[1]:
  x[0]*=3
  x[1]*=2
  c+=1
print(c)
