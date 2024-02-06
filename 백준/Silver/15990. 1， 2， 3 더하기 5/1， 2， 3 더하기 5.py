import sys

limit = 100000
li = [[0]*4 for _ in range(limit+1)]
mod = 1000000009
li[1] = [0, 1, 0, 0]
li[2] = [0, 0, 1, 0]
li[3] = [0, 1, 1, 1]

for i in range(4, 100001):
    li[i][1] = (li[i-1][2] + li[i-1][3])%mod
    li[i][2] = (li[i-2][1] + li[i-2][3])%mod
    li[i][3] = (li[i-3][1] + li[i-3][2])%mod

T = int(sys.stdin.readline())
for _ in range(T):
    sys.stdout.write(str(sum(li[int(sys.stdin.readline())])%mod)+'\n')