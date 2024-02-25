import sys
from collections import deque


def solution(N, M, V, dic):
    def dfs(x):
        tf_dfs[x] = True
        ans_dfs.append(x)
        for i in dic[x]:
            if tf_dfs[i] == False:
                dfs(i)

    def bfs(x):
        ans = []
        que = deque([])
        que.append(x)
        tf_bfs[x] = True
        ans.append(x)
        while que:
            n = que.popleft()
            for i in dic[n]:
                if tf_bfs[i] == False:
                    que.append(i)
                    tf_bfs[i] = True
                    ans.append(i)
        return ans

    tf_dfs = [False] * (N + 1)
    ans_dfs = []
    dfs(V)
    print(*ans_dfs)
    tf_bfs = [False] * (N + 1)
    print(*bfs(V))


N, M, V = map(int, sys.stdin.readline().split())
dic = {n: [] for n in range(N + 1)}
readlines = sys.stdin.readlines()
for readline in readlines:
    x, y = map(int, readline.split())
    dic[x].append(y)
    dic[y].append(x)

for v in dic.values():
    v.sort()

solution(N, M, V, dic)
