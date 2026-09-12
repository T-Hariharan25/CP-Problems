x=int(input())
y=list(map(int, input().split()))
z=[]
for i in y:
    if i<0:
        z.append(2)
    elif i>0:
        z.append(1)
    else:
        z.append(0)
print(*z)                