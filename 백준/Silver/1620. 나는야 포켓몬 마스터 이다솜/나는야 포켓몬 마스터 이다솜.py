import sys


N, M = map(int, sys.stdin.readline().split())
dic1 = {}
dic2 = {}
for n in range(1, N+1):
    x = sys.stdin.readline().strip()
    dic1[str(n)] = x
    dic2[x] = str(n)
# dic = {str(n): sys.stdin.readline().strip() for n in range(1, N+1)}


for _ in range(M):
    x = sys.stdin.readline().strip()
    if x.isdecimal():
        sys.stdout.write(dic1[x] + '\n')
    else:
        sys.stdout.write(dic2[x] + '\n')