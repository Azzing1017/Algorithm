import sys

N = int(sys.stdin.readline())
li = [0] * 10001
for _ in range(N):
    li[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    cnt = li[i]
    for _ in range(cnt):
        sys.stdout.write(str(i)+'\n')
