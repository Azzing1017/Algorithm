from collections import deque

N, K = map(int, input().split())
li = [-1] * 100001
que = deque([N])
li[N] = 0
while que:
    x = que.popleft()
    if x == K:
        print(li[K])
        break
    if 0<= x*2 <=100000 and li[x*2] == -1:
        li[x*2] = li[x]
        que.appendleft(x*2)
    if 0<= x-1 <=100000 and li[x-1] == -1:
        li[x-1] = li[x] + 1
        que.append(x-1)
    if 0<= x+1 <=100000 and li[x+1] == -1:
        li[x+1] = li[x] + 1
        que.append(x+1)