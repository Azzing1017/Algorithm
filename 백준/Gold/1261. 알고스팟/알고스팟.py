from collections import deque

M, N = map(int, input().split())
li = [list(map(int, list(input()))) for _ in range(N)]
ans = [[10000]*M for _ in range(N)]
ans[0][0] = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
que = deque([[0,0]])

while que:
    x, y = que.popleft()
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0<= nx <N and 0<= ny <M:
            if li[nx][ny] == 0 and ans[nx][ny] > ans[x][y]:
                ans[nx][ny] = ans[x][y]
                que.append([nx, ny])
            elif li[nx][ny] == 1 and ans[nx][ny] > ans[x][y] + 1:
                ans[nx][ny] = ans[x][y] + 1
                que.append([nx, ny])

print(ans[N-1][M-1])