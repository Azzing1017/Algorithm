import sys

N = int(sys.stdin.readline().strip())
li = list([i, int(x), 0] for i, x in enumerate(sys.stdin.readline().split()))
li.sort(key=lambda x:x[1])

cur = li[0][1]
num = 0
for i in range(1, N):
    if li[i][1] == cur:
        li[i][2] = num
    elif li[i][1] > cur:
        cur = li[i][1]
        num += 1
        li[i][2] = num
li.sort(key=lambda x:x[0])

for var in li:
    sys.stdout.write(str(var[2]) + ' ')