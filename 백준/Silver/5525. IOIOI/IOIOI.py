import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()

i = 0
cnt = 0
ans = 0
while i+3 <= M:
    if S[i:i + 3] == 'IOI':
        cnt += 1
        i += 2
        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        cnt = 0
        i += 1

sys.stdout.write(str(ans))
