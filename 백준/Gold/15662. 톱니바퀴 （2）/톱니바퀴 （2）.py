import sys
from collections import deque

read_lines = sys.stdin.readlines()
T = int(read_lines[0].strip())
arr = deque([deque(list(read_line.strip())) for read_line in read_lines[1:T+1]])
K = int(read_lines[T+1].strip())
com = deque([list(map(int, read_line.split())) for read_line in read_lines[T+2:T+2+K]])

while com:
    n, r = com.popleft()
    n = n-1
    li = [0]*T
    li[n] = r
    for a in range(n+1, T):
        if arr[a][6] != arr[a-1][2]:
            if (a-n)%2 == 1:
                li[a] = -r
            else:
                li[a] = r
        else:
            break
    for b in range(n-1, -1, -1):
        if arr[b][2] != arr[b+1][6]:
            if (n-b)%2 == 1:
                li[b] = -r
            else:
                li[b] = r
        else:
            break
    for i in range(T):
        arr[i].rotate(li[i])
cnt = 0
for val in arr:
    if val[0] == '1':
        cnt += 1

sys.stdout.write(str(cnt))