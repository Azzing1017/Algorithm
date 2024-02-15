import sys


def go(N):
    if N == 1:
        return 1
    else:
        return N + go(N-1)


while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    else:
        sys.stdout.write(str(go(n))+'\n')