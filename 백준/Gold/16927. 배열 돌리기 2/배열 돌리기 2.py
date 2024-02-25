import sys
from collections import deque

readlines = sys.stdin.readlines()
N, M, R = map(int, readlines[0].split())
arr = [list(readline.split()) for readline in readlines[1:]]

for i in range(min(N//2, M//2)):
    que = deque([])
    for a in range(i, N-1-i):
        que.append(arr[a][i])
    for b in range(i, M-1-i):
        que.append(arr[N-1-i][b])
    for c in range(N-1-i, i, -1):
        que.append(arr[c][M-1-i])
    for d in range(M-1-i, i, -1):
        que.append(arr[i][d])
    que.rotate(R%len(que))
    for a in range(i, N-1-i):
        arr[a][i] = que.popleft()
    for b in range(i, M-1-i):
        arr[N-1-i][b] = que.popleft()
    for c in range(N-1-i, i, -1):
        arr[c][M-1-i] = que.popleft()
    for d in range(M-1-i, i, -1):
        arr[i][d] = que.popleft()

sys.stdout.write('\n'.join(map(str, [' '.join(li) for li in arr])))
