import sys

N = int(sys.stdin.readline().strip())
arr = [0] + [int(sys.stdin.readline().strip()) for _ in range(N)]
li = [[0, 0] for _ in range(N+1)]
li[1] = [arr[1], 0]
if N >= 2:
    li[2] = [arr[2], arr[1]+arr[2]]
if N >= 3:
    for i in range(3, N+1):
        li[i][0] = max(li[i-2][0], li[i-2][1]) + arr[i]
        li[i][1] = li[i-1][0] + arr[i]

sys.stdout.write(str(max(li[N][0], li[N][1])))