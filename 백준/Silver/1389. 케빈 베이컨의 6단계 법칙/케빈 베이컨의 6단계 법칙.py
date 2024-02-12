import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)
li = [[0] * (N + 1) for _ in range(N + 1)]
ans = 0
ans_min = 10000
que = deque([])
for i in range(1, N+1):
    tf = [False] * (N + 1)
    tf[i] = True
    que.append([i, 0])
    while que:
        x, cnt = que.popleft()
        cnt += 1
        for j in arr[x]:
            if not tf[j]:
                tf[j] = True
                li[i][j] = cnt
                que.append([j, cnt])
    sum_check = sum(li[i])
    if ans_min > sum_check:
        ans_min = sum_check
        ans = i

sys.stdout.write(str(ans))