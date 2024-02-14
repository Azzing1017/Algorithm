import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()
NS = 'I' + 'OI'*N

cnt = 0
while True:
    x = S.find(NS)
    if x == -1:
        break
    else:
        cnt += 1
        S = S[x+2:]

sys.stdout.write(str(cnt))