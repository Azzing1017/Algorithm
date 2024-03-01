from collections import deque

N, K = map(int, input().split())
dist = deque(list(map(int, input().split())))
n = deque([0 for _ in range(N*2)])
cur = 0
cnt = 0
while cnt < K:
    cur += 1
    dist.rotate(1)
    n.rotate(1)
    if n[N-1] == 1:
        n[N-1] = 0
    for idx in range(0, -N*2, -1):
        if n[idx] == 0 and dist[idx] != 0 and n[idx-1] == 1:
            n[idx-1] = 0
            n[idx] = 1
            dist[idx] -= 1
            if dist[idx] == 0:
                cnt += 1
    if n[N-1] == 1:
        n[N-1] = 0
    if n[0] == 0 and dist[0] != 0:
        n[0] = 1
        dist[0] -= 1
        if dist[0] == 0:
            cnt += 1

print(cur)
