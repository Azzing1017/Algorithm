import sys
from collections import deque

read_lines = sys.stdin.readlines()
N, M, x, y, K = map(int, read_lines[0].split())
arr = [list(map(int, read_line.split())) for read_line in read_lines[1:N+1]]
coms = deque(list(map(int, read_lines[-1].split())))
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

while coms:
    com = coms.popleft()
    nx = x + dx[com]
    ny = y + dy[com]
    if 0 <= nx < N and 0 <= ny < M:
        x = nx
        y = ny
        if com == 1:
            dice[0], dice[2], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[2]
        elif com == 2:
            dice[0], dice[2], dice[4], dice[5] = dice[4], dice[5], dice[2], dice[0]
        elif com == 3:
            dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
        elif com == 4:
            dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
        if arr[x][y] == 0:
            arr[x][y] = dice[2]
        else:
            dice[2] = arr[x][y]
            arr[x][y] = 0
        sys.stdout.write(str(dice[0]) + '\n')
