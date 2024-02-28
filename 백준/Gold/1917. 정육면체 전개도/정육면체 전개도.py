from collections import deque

arr1 = [list(map(int, input().split())) for _ in range(6)]
arr2 = [list(map(int, input().split())) for _ in range(6)]
arr3 = [list(map(int, input().split())) for _ in range(6)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def go(arr):
    for a in range(6):
        for b in range(6):
            if arr[a][b] == 1:
                return [a, b]


def gogo(arr, x, y, dice):
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < 6 and 0 <= ny < 6 and arr[nx][ny] == 1:
            arr[nx][ny] = 2
            if idx == 0:
                dice[0],dice[1],dice[2],dice[3] = dice[3],dice[0],dice[1],dice[2]
            elif idx == 1:
                dice[0],dice[1],dice[2],dice[3] = dice[1],dice[2],dice[3],dice[0]
            elif idx == 2:
                dice[0],dice[2],dice[4],dice[5] = dice[4],dice[5],dice[2],dice[0]
            elif idx == 3:
                dice[0],dice[2],dice[4],dice[5] = dice[5],dice[4],dice[0],dice[2]
            dice[0] = 1
            gogo(arr, nx, ny, dice)
            if idx == 0:
                dice[3],dice[0],dice[1],dice[2] = dice[0],dice[1],dice[2],dice[3]
            elif idx == 1:
                dice[1],dice[2],dice[3],dice[0] = dice[0],dice[1],dice[2],dice[3]
            elif idx == 2:
                dice[4],dice[5],dice[2],dice[0] = dice[0],dice[2],dice[4],dice[5]
            elif idx == 3:
                dice[5],dice[4],dice[0],dice[2] = dice[0],dice[2],dice[4],dice[5]


for arr in [arr1, arr2, arr3]:
    x, y = go(arr)
    dice = [1, 0, 0, 0, 0, 0]
    arr[x][y] = 2
    gogo(arr, x, y, dice)
    if sum(dice) == 6:
        print('yes')
    else:
        print('no')

