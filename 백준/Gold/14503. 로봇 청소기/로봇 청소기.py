import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
arr = [list(map(int, read_line.split())) for read_line in sys.stdin.readlines()]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0
while 0 <= r < N and 0 <= c < M:
    if arr[r][c] == 0:
        arr[r][c] = -1
        cnt += 1
    check = False
    for idx in range(d-1, d-5, -1):
        nr = r + dr[idx]
        nc = c + dc[idx]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 0:
                check = True
                r, c = nr, nc
                d = idx
                if d == -4:
                    d = 0
                elif d == -3:
                    d = 1
                elif d == -2:
                    d = 2
                elif d == -1:
                    d = 3
                break
    if not check:
        nr = r + dr[d-2]
        nc = c + dc[d-2]
        if arr[nr][nc] == 1:
            break
        r, c = nr, nc

sys.stdout.write(str(cnt))