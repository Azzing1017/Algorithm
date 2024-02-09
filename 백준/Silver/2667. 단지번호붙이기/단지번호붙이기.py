from collections import deque

N = int(input())
li = [list(input()) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
que = deque([])

cnt = 0
ans = []
for i in range(N):
    for j in range(N):
        if li[i][j] == '1':
            li[i][j] = '0'
            que.append([i, j])
            ans.append(1)
            while que:
                x, y = que.pop()
                for idx in range(4):
                    nx = x + dx[idx]
                    ny = y + dy[idx]
                    if 0<= nx < N and 0<= ny < N:
                        if li[nx][ny] == '1':
                            que.append([nx, ny])
                            li[nx][ny] = '0'
                            ans[cnt] += 1
            cnt += 1

print(cnt)
ans.sort()
print('\n'.join(map(str, ans)))