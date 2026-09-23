x=list(map(int, input().split()))
s=list(map(int, input().split()))
c=0
for i in s:
  if i>=s[x[1]-1] and i>0:
    c+=1
print(c)