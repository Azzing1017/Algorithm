import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(x + y) + '\n')
    