N, c, r = map(int, input().split())

def go(count, N, c, r):

    x = 0

    mid = 2**(N-1)-1

    if c > mid:
        x += 2
    if r > mid:
        x += 1

    if N == 1:
        return count + x
    else:
        cnt = 2**(N-1) * 2**(N-1) * x
        if x==2 or x==3:
            c = c - 2**(N-1)
        if x==1 or x==3:
            r = r - 2**(N-1)
        return go(count + cnt, N-1, c, r)

print(go(0, N, c, r))