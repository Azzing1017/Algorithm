import sys

N, M = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li_sum = [0]*(N+1)
for i in range(1, N+1):
    li_sum[i] += li_sum[i-1] + li[i-1]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(li_sum[y] - li_sum[x-1])+'\n')