x=int(input())
y=list(map(int, input().split()))
for i in range(len(y)-1,0,-1):
  for j in range(i):
    if y[j]>y[j+1]:
      y[j],y[j+1]=y[j+1],y[j]
      
print(*y)