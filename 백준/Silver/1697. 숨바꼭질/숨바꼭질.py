# 1696
from collections import deque

N, K = map(int, input().split())
li = [0] * 100001
que = deque([])

que.append(N)
ans = 0
while que:
    x = que.popleft()
    if x == K:
        ans = li[K]
        break
    for nx in [x+1, x-1, x*2]:
        if 0<= nx <=100000:
            if not li[nx] or li[nx] > li[x] + 1:
                li[nx] = li[x] + 1
                que.append(nx)

print(ans)