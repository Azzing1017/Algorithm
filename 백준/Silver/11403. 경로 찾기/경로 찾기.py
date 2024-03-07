N = int(input())
INF_POS = float('inf')
arr = [list(map(int, input().split())) for _ in range(N)]


for n in range(N):
    for m in range(N):
        if arr[n][m] == 0:
            arr[n][m] = INF_POS


for k in range(N):
    for a in range(N):
        for b in range(N):
            arr[a][b] = min(arr[a][b], arr[a][k]+arr[k][b])


for i in range(N):
    for j in range(N):
        if arr[i][j] == INF_POS:
            arr[i][j] = 0
        elif arr[i][j] != 0:
            arr[i][j] = 1


for ar in arr:
    print(*ar)
    