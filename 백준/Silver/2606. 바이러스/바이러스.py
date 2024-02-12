import sys
from collections import deque

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
li = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    li[x].append(y)
    li[y].append(x)
tf = [False]*(N+1)

que = deque([1])
tf[1] = True
while que:
    x = que.popleft()
    for i in li[x]:
        if not tf[i]:
            que.append(i)
            tf[i] = True

cnt = 0
for i in range(2, N+1):
    if tf[i]:
        cnt += 1
sys.stdout.write(str(cnt))
