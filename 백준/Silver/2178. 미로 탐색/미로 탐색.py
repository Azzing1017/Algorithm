from collections import deque

N, M = map(int, input().split())
li = [list(map(int, list(input()))) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

que = deque([[0, 0]])

while que:
    x, y = que.popleft()
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0<= nx < N and 0<= ny < M:
            if li[nx][ny] == 1:
                que.append([nx, ny])
                li[nx][ny] = li[x][y] + 1

print(li[N-1][M-1])