import sys

N, M = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))


def go(st, ed):
    global li, N, M
    if st > ed:
        return ed
    else:
        md = (st + ed) // 2
        total = 0
        for i in range(0, N):
            if li[i] > md:
                total = total + li[i] - md
        if total >= M:
            return go(md+1, ed)
        elif total < M:
            return go(st, md-1)


sys.stdout.write(str(go(0, max(li))))
