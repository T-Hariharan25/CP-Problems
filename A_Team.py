x=int(input())
c=0
s=[list(map(int,input().split())) for _ in range(x)]
for i in s:
  if sum(i)>=2:
    c+=1
print(c)
  