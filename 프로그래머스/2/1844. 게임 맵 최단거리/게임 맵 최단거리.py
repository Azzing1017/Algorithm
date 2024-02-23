from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    que = deque([])
    que.append([0, 0])
    while que:
        x, y = que.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] != 0:
                    if maps[nx][ny] == 1 or maps[nx][ny] > maps[x][y] + 1:
                        maps[nx][ny] = maps[x][y] + 1
                        que.append([nx, ny])
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]