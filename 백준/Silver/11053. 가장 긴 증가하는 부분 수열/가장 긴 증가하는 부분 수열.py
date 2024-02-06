N = int(input())
A = list(map(int, input().split()))
D = [1]*N
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            if D[i] < D[j]+1:
                D[i] = D[j] + 1
D.sort()
print(D.pop())