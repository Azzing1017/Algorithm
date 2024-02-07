N, K = map(int, input().split())
li_fac = [1]*(N+K)

for i in range(2, N+K):
    li_fac[i] = li_fac[i-1]*i

res = li_fac[N+K-1]//(li_fac[N+K-1-(K-1)]*li_fac[K-1])
res = res%1000000000
print(res)