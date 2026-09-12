x=int(input())
y=list(map(int, input().split()))
z=int(input())
if z in y:
    print(y.index(z))
else:
    print('-1')