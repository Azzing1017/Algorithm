dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def go(li_tf, x, y):
    global dx, dy
    queue = []
    queue.append([x, y])
    li_tf[x][y] = False
    while queue:
        a, b = queue.pop()
        li_tf[a][b] = False
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<= nx <N and 0<= ny <M:
                if li_tf[nx][ny]:
                    queue.append([nx, ny])

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    li_tf = [[False]*M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        li_tf[x][y] = True

    cnt = 0
    for i in range(N):
        for j in range(M):
            if li_tf[i][j]:
                cnt += 1
                go(li_tf, i, j)

    print(cnt)