import sys
from collections import deque

N = int(sys.stdin.readline().strip())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
li.sort(key=lambda x: (x[0], x[1]))
li = deque(li)
cnt = 0
st = 0
while li:
    x, y = li.popleft()
    if y < st:
        st = y
    elif x >= st:
        cnt += 1
        st = y

sys.stdout.write(str(cnt))
