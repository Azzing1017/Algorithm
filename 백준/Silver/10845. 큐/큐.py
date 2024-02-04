import sys
from collections import deque

N = int(sys.stdin.readline())
li = []
que_li = deque([])
for _ in range(N):
    order, *num = map(str, sys.stdin.readline().split())
    X = 0
    if num:
        X = num[0]
    if order == 'push':
        que_li.append(X)
    elif order == 'pop':
        if que_li:
            sys.stdout.write(que_li.popleft()+'\n')
        else:
            sys.stdout.write('-1'+'\n')
    elif order == 'size':
        sys.stdout.write(str(len(que_li))+'\n')
    elif order == 'empty':
        if que_li:
            sys.stdout.write('0'+'\n')
        else:
            sys.stdout.write('1'+'\n')
    elif order == 'front':
        if que_li:
            sys.stdout.write(que_li[0]+'\n')
        else:
            sys.stdout.write('-1'+'\n')
    elif order == 'back':
        if que_li:
            sys.stdout.write(que_li[-1]+'\n')
        else:
            sys.stdout.write('-1'+'\n')
    else:
        break