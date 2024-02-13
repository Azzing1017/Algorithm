import sys
from collections import deque

T = int(sys.stdin.readline().strip())
for _ in range(T):
    cmd = deque(sys.stdin.readline().strip())
    N = int(sys.stdin.readline().strip())
    li = deque(map(int, filter(None, sys.stdin.readline().strip('[]\n').split(','))))
    cnt = 0
    check = True
    while cmd:
        x = cmd.popleft()
        if x == 'R':
            cnt += 1
        elif x == 'D':
            if li:
                if cnt % 2 == 0:
                    li.popleft()
                elif cnt % 2 == 1:
                    li.pop()
            else:
                sys.stdout.write('error' + '\n')
                check = False
                break
    if check:
        if cnt % 2 == 1:
            li.reverse()
        sys.stdout.write('['+','.join(map(str, li))+']'+'\n')
