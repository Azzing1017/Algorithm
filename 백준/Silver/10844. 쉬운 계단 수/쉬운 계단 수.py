import sys

N = int(sys.stdin.readline())
mod = 1000000000
li = [[0]*10 for _ in range(N+1)]
li[1] = [1,1,1,1,1,1,1,1,1,1]
for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            li[i][j] = (li[i-1][j+1])%mod
        elif j == 9:
            li[i][j] = (li[i-1][j-1])%mod
        else:
            li[i][j] = (li[i-1][j+1] + li[i-1][j-1])%mod

sys.stdout.write(str(sum(li[N][1:10])%mod))