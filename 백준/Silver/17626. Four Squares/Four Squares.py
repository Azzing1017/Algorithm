n = int(input())

INF_POS = float('inf')

dp = [INF_POS] * (n+1)
dp[0] = 0
for i in range(1, int(n**(1/2))+1):
    dp[i*i] = 1

for a in range(1, n+1):
    for b in range(1, int(a**(1/2))+1):
        dp[a] = min(dp[a], dp[a-b**2]+1)

print(dp[-1])
