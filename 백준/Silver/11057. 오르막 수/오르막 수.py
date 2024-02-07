mod = 10007
N = int(input())
li = [[0]*10 for _ in range(N+1)]
li[1] = [1]*10
for i in range(1, N+1):
    for j in range(10):
        for k in range(j+1):
            li[i][j] += li[i-1][k]%mod

print(sum(li[N])%10007)