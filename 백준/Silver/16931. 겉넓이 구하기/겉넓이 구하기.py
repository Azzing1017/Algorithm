import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, read_line.split())) for read_line in sys.stdin.readlines()]
da = [0, 0, -1, 1]
db = [-1, 1, 0, 0]

ans = N*M*2
for a in range(N):
    for b in range(M):
        for idx in range(4):
            na = a +da[idx]
            nb = b +db[idx]
            if 0 <= na < N and 0 <= nb < M:
                if arr[a][b] > arr[na][nb]:
                    ans += arr[a][b] - arr[na][nb]
            else:
                ans += arr[a][b]

sys.stdout.write(str(ans))
