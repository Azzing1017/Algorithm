N, K = map(int, input().split())
li = [[0]*(N+1) for _ in range(K+1)]
li[0][0] = 1
mod = 1000000000

for i in range(1, K+1):
    for j in range(N+1):
        for l in range(j+1):
            li[i][j] += li[i-1][j-l]
        li[i][j] %= mod

print(li[K][N])