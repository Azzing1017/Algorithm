import sys
input = sys.stdin.readline
x_max = 20
M = int(input())
S = 0
for _ in range(M):
    op, *num = input().split()
    x = 0
    if len(num) != 0:
        x = int(num[0])-1
    if op == 'add':
        S = (S | (1<<x))
    elif op == 'remove':
        S = (S & ~(1<<x))
    elif op == 'check':
        res = (S & (1<<x))
        if res != 0:
            sys.stdout.write('1'+'\n')
        else:
            sys.stdout.write('0'+'\n')
    elif op == 'toggle':
        S = (S ^ (1<<x))
    elif op == 'all':
        S = (1<<x_max) - 1
    elif op == 'empty':
        S = 0
    else:
        break