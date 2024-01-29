case = int(input())

def gcd_cal(M, N):
    if min(M, N) == 0:
        return max(M, N)
    else:
        return gcd_cal(min(M, N), max(M, N)%min(M, N))

for _ in range(case):
    M, N, x, y = map(int, input().split())
    gcd = gcd_cal(M, N)
    lcm = int(M / gcd * N)
    year = -1
    k = x
    for i in range(k, lcm+1, M):
        b = i % N
        if b == 0:
            b = N
        if y == b:
            year = i
            break
    print(year)