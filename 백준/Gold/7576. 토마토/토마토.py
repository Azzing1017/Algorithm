from collections import deque
import sys

M, N = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

que = deque([])

cnt = 0
for i in range(N):
    for j in range(M):
        if li[i][j] == 1:
            que.append([i, j])
            cnt += 1
        elif li[i][j] == -1:
            cnt += 1

ans_x = 0
ans_y = 0
while que:
    x, y = ans_x, ans_y = que.popleft()
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0<= nx < N and 0<= ny < M:
            if li[nx][ny] == 0:
                li[nx][ny] = li[x][y] + 1
                que.append([nx, ny])
                cnt += 1

if cnt == N * M:
    sys.stdout.write(str(li[ans_x][ans_y] - 1))
else:
    sys.stdout.write(str(-1))
