from collections import deque


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
tf = [[True] * M for _ in range(N)]


que = deque([])
for a in range(N):
    for b in range(M):
        if arr[a][b] == 'I':
            que.append([a, b])
            tf[a][b] = False
        if que:
            break
    if que:
        break


cnt = 0
while que:
    x, y = que.popleft()
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < N and 0 <= ny < M and tf[nx][ny] and arr[nx][ny] != 'X':
            if arr[nx][ny] == 'P':
                cnt += 1
            que.append([nx, ny])
            tf[nx][ny] = False


if cnt == 0:
    print('TT')
else:
    print(cnt)
    