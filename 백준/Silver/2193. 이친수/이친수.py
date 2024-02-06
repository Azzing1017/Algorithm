import sys

N = int(sys.stdin.readline())
li = [[0]*2 for _ in range(N+1)]
li[1][1] = 1
for i in range(2, N+1):
    li[i][0] = sum(li[i-1])
    li[i][1] = li[i-1][0]

sys.stdout.write(str(sum(li[N])))