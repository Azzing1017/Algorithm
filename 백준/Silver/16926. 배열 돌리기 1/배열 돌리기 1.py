import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(min(N//2, M//2)):
    que = deque([])
    for a in range(i, M-i-1):
        que.append(arr[i][a])
    for b in range(i, N-i-1):
        que.append(arr[b][M-i-1])
    for c in range(M-i-1, i, -1):
        que.append(arr[N-i-1][c])
    for d in range(N-i-1, i, -1):
        que.append(arr[d][i])
    que.rotate(-R)
    for a in range(i, M-i-1):
        arr[i][a] = que.popleft()
    for b in range(i, N-i-1):
        arr[b][M-i-1] = que.popleft()
    for c in range(M-i-1, i, -1):
        arr[N-i-1][c] = que.popleft()
    for d in range(N-i-1, i, -1):
        arr[d][i] = que.popleft()

for val in arr:
    print(*val)