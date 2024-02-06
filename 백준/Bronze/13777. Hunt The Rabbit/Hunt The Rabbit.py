li = [n for n in range(51)]
li_ans = []

def go(st, ed, n):
    global li, li_ans
    if st > ed:
        return
    else:
        cen = (st+ed)//2
        li_ans.append(cen)
        if li[cen] == n:
            return
        elif li[cen] > n:
            return go(st, cen-1, n)
        elif li[cen] < n:
            return go(cen+1, ed, n)

while True:
    n = int(input())
    if n == 0:
        break
    else:
        li_ans = []
        go(1, 50, n)
        print(' '.join(map(str, li_ans)))