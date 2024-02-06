n = int(input())
A = list(map(int, input().split()))
D = [-1000*100000]*n

for i in range(n):
    D[i] = max(A[i], D[i-1]+A[i])

D.sort()
print(D.pop())