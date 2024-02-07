N = int(input())
cnt = 0
if N % 2 == 1:
    cnt = 0
else:
    li = [0] * (N+1)
    for i in range(2, N+1, 2):
        if i == 2:
            li[2] = 3
        else:
            li[i] = li[i-2]*3 + 2
            for j in range(4, i, 2):
                li[i] += li[i-j]*2
    cnt = li[N]

print(cnt)