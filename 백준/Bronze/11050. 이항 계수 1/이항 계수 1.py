N, K = map(int, input().split())

def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)

def com(N, K):
    return fac(N)/(fac(N-K)*fac(K))

print(int(com(N, K)))