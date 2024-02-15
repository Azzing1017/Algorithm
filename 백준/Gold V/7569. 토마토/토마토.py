import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
arr = [list(list(map(int, sys.stdin.readline().split())) for _ in range(N)) for _ in range(H)]

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

cnt = 0
que = deque([])
for z in range(H):
    for y in range(N):
        for x in range(M):
            if arr[z][y][x] == 1:
                que.append([z, y, x])
                cnt += 1
            elif arr[z][y][x] == -1:
                cnt += 1
ans = 0
if cnt == M * N * H:
    sys.stdout.write('0')
else:
    while que:
        z, y, x = que.popleft()
        for idx in range(6):
            nx = x + dx[idx]
            ny = y + dy[idx]
            nz = z + dz[idx]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if arr[nz][ny][nx] == 0:
                    arr[nz][ny][nx] = ans = arr[z][y][x] + 1
                    que.append([nz, ny, nx])
                    check = True
                    cnt += 1
                else:
                    continue
    if cnt == M * N * H:
        sys.stdout.write(str(ans - 1))
    else:
        sys.stdout.write('-1')
