import sys
from collections import deque

readlines = sys.stdin.readlines()
N, M = map(int, readlines[0].strip().split())
dic = {n: [] for n in range(N+1)}
for readline in readlines[1:]:
    x, y = map(int, readline.strip().split())
    dic[x].append(y)
    dic[y].append(x)


def dfs(num_cur):
    visited[num_cur] = 1
    for num_next in dic[num_cur]:
        if visited[num_next] == 0:
            dfs(num_next)


visited = [0] * (N+1)
cnt_dfs = 0
for i in range(1, N+1):
    if visited[i] == 0:
        cnt_dfs += 1
        dfs(i)

sys.stdout.write(str(cnt_dfs))

# 
# def bfs(num_start):
#     que = deque([])
#     que.append(num_start)
#     visited[num_start] = 1
#     while que:
#         num_cur = que.popleft()
#         for num_next in dic[num_cur]:
#             if visited[num_next] == 0:
#                 visited[num_next] = 1
#                 que.append(num_next)
# 
# 
# visited = [0] * (N + 1)
# cnt_bfs = 0
# for i in range(1, N+1):
#     if visited[i] == 0:
#         cnt_bfs += 1
#         bfs(i)
# 
# sys.stdout.write(str(cnt_bfs))
