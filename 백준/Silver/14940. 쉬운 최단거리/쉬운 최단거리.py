import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
tf = [[False]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

que = deque([])
for i in range(n):
    for j in range(m):
        if li[i][j] == 2:
            que.append([i, j])
            li[i][j] = 0
            tf[i][j] = True
            break

while que:
    x, y = que.popleft()
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < n and 0 <= ny < m:
            if li[nx][ny] != 0:
                if not tf[nx][ny]:
                    li[nx][ny] = li[x][y] + 1
                    tf[nx][ny] = True
                    que.append([nx, ny])
            else:
                tf[nx][ny] = True

for i in range(n):
    for j in range(m):
        if not tf[i][j]:
            if li[i][j] == 1:
                li[i][j] = -1

sys.stdout.write('\n'.join([' '.join(map(str, row)) for row in li])+'\n')