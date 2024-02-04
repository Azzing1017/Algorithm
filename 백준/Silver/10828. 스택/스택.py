import sys

N = int(sys.stdin.readline())
S = []
for _ in range(N):
    order, *li = map(str, sys.stdin.readline().split())
    X = 0
    if li:
        X = li[0]
    if order == 'push':
        S.append(X)
    elif order == 'pop':
        if S:
            sys.stdout.write(S.pop()+'\n')
        else:
            sys.stdout.write('-1'+'\n')
    elif order == 'size':
        sys.stdout.write(str(len(S))+'\n')
    elif order == 'empty':
        if S:
            sys.stdout.write('0'+'\n')
        else:
            sys.stdout.write('1'+'\n')
    elif order == 'top':
        if S:
            sys.stdout.write(S[-1]+'\n')
        else:
            sys.stdout.write('-1'+'\n')
    else:
        break