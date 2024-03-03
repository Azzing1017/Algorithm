T = int(input())
li = [list(map(int, input().split())) for _ in range(T)]

for N, M in li:
    if N == 0:
        print(0)
    else:
        n = 1
        m = 1
        for a in range(1, N+1):
            n *= a
        for b in range(M-N+1, M+1):
            m *= b
        print(m//n)