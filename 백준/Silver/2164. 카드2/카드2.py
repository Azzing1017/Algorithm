import sys
from collections import deque

N = int(sys.stdin.readline())
li = [n for n in range(1, N+1)]
dq_li = deque(li)
len_li = N

while len_li > 1:
    dq_li.popleft()
    dq_li.rotate(-1)
    len_li -= 1

sys.stdout.write(str(dq_li.pop()))