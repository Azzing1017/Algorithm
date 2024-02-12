import sys


N = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# li = [list(map(int, line.split())) for line in sys.stdin.readlines()]


wcnt = 0
bcnt = 0


def go(list, N):
    global wcnt, bcnt
    check = False
    check0 = list[0][0]
    for i in range(N):
        for j in range(N):
            if list[i][j] != check0:
                check = True
    if check:
        li_1 = list[0:N // 2]
        li_4 = list[N // 2:N]
        li_2 = [[] for _ in range(N // 2)]
        li_3 = [[] for _ in range(N // 2)]
        for i in range(N // 2):
            li_2[i] = li_1[i][N // 2:N]
            li_3[i] = li_4[i][N // 2:N]
            li_1[i] = li_1[i][0:N // 2]
            li_4[i] = li_4[i][0:N // 2]
        go(li_1, N // 2)
        go(li_2, N // 2)
        go(li_3, N // 2)
        go(li_4, N // 2)
    else:
        if check0 == 0:
            wcnt += 1
        elif check0 == 1:
            bcnt += 1


go(li, N)
sys.stdout.write(str(wcnt)+'\n'+str(bcnt))