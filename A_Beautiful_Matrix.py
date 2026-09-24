for i in range(1,6):
  c=list(map(int,input().split()))
  if 1 in c:
     r=c.index(1)+1
     print(abs(i-3)+abs(r-3))