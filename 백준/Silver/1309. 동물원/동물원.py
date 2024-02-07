mod = 9901

N = int(input())
li = [[0,0,0] for _ in range(N+1)]
li[1] = [1,1,1]

for i in range(2, N+1):
    li[i][0] = (sum(li[i-1]))%mod
    li[i][1] = (li[i-1][0]+li[i-1][2])%mod
    li[i][2] = (li[i-1][0]+li[i-1][1])%mod

print(sum(li[N])%mod)