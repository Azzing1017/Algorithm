from collections import deque

N, M = map(int, input().split())
li = [[]for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    li[x].append(y)
    li[y].append(x)
tf = [False] * (N+1)
que = deque([])
cnt = 0
for i in range(1, N+1):
    if tf[i]:
        continue
    else:
        que.append(i)
        tf[i] = True
        cnt += 1
        while que:
            temp = que.popleft()
            for j in li[temp]:
                if tf[j]:
                    continue
                else:
                    que.append(j)
                    tf[j] = True

print(cnt)

