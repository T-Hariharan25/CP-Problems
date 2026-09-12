x = int(input()) 
A = list(map(int, input().split()))
print(min(A),A.index(min(A))+1)