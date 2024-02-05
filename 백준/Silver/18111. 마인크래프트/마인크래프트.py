N, M, B = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
li_ans = []

sum_all = 0
num_max = 0
for val in li:
    sum_all += sum(val)
    for n in val:
        if n > num_max:
            num_max = n
st = sum_all//(N*M)

while st <= num_max:
    cnt = 0
    ti = 0
    for i in range(N):
        for j in range(M):
            tmp = li[i][j] - st
            cnt = cnt + tmp
            if tmp > 0:
                ti = ti + tmp*2
            else:
                ti = ti + abs(tmp)
    if cnt + B >= 0:
        li_ans.append([ti, st])
        st += 1
    else:
        break

li_ans.sort(key=lambda x:(x[0], -x[1]))
print(*li_ans[0])